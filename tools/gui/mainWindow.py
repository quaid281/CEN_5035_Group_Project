#!/usr/bin/python3

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread

import os
import sys
import cv2
import numpy as np

sys.path.append("../cloud")
sys.path.append("../camera")
sys.path.append("../model")
import cameraLib
import gcp_upload
import predictImage
 
import time
import math

class VideoThread(QThread):

    # Thread needs a signal whenever a new frame has been read from the camera
    change_pixmap_signal = pyqtSignal(np.ndarray)

    cam = cv2.VideoCapture(cameraLib.sci_cam_params(), cv2.CAP_GSTREAMER)

    model = predictImage.loadModel()
    classes = predictImage.loadClasses()
    last_date = math.floor(time.time())

    def run(self):
        while True:
            ret, img = self.cam.read()
            if ret:
                # Emit image so we can grab with update_image
                self.change_pixmap_signal.emit(img)

            self.img = img

            self.date = math.floor(time.time())
            
             # Only predict once per second
            if (self.date > self.last_date): 
                self.predict = True

            if (self.predict):
                resize = cv2.resize(img, (150, 150), interpolation=cv2.INTER_CUBIC)
                print(predictImage.predictImage(resize, self.model, self.classes))
                self.last_date = self.date
                self.predict = False


class App(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setWindowTitle("Hand Gesture Capture")
        self.disply_width = 640
        self.display_height = 480

        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)


        self.thread = VideoThread()

        self.lastPhoto = None

        self.takeImage = QPushButton("Take Photo", self)
        self.takeImage.clicked.connect(self.save_image)
        self.uploadImage = QPushButton("Upload Photos", self)
        self.uploadImage.clicked.connect(self.upload_last_image)

        # Vbox for Video
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)

        # Hbox for buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.takeImage)
        hbox.addWidget(self.uploadImage)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # create the video capture thread
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()


    def update_image(self, img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(img)
        self.image_label.setPixmap(qt_img)


    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

 
    def save_image(self):
        self.lastPhoto = cameraLib.saveImage(self.thread.img)


    def upload_last_image(self):
        if (self.lastPhoto):
            gcp_upload.upload_blob("iot-project_healthy-cubist-326609",
                                    "/usr/share/CEN5035/service_account.json",
                                    self.lastPhoto,
                                    self.lastPhoto)

   
if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())
