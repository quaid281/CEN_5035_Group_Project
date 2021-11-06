#!/usr/bin/python3

import cv2
import time


def sci_cam_params(
    capture_width=1920,
    capture_height=1080,
    display_width=1920,
    display_height=1080,
    framerate=30,
    flip_method=2,
):
    return(
    "nvarguscamerasrc ! "
    "video/x-raw(memory:NVMM), "
    "width=(int)%d, height=(int)%d, "
    "format=(string)NV12, framerate=(fraction)%d/1 ! "
    "nvvidconv flip-method=%d ! "
    "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
    "videoconvert ! "
    "video/x-raw, format=(string)BGR ! appsink" %
        (capture_width,
         capture_height,
         framerate,
         flip_method,
         display_width,
         display_height,
        )
    )

def generateImageName(name="UNCLASSIFIED"):
    t = time.gmtime()
    return str(name + "-%04d-%02d-%02d-%02d:%02d:%02d.jpg" % (t.tm_year,
                                                t.tm_mon,
                                                t.tm_mday,
                                                t.tm_hour,
                                                t.tm_min,
                                                t.tm_sec))

def captureImage(cam=None, delay=0.0, capture_width=1920, capture_height=1080):

    if not cam:
        cam = cv2.VideoCapture(sci_cam_params(capture_width, capture_height), cv2.CAP_GSTREAMER)
        #cam = cv2.VideoCapture("v4l2src device=/dev/video0 ! videoconvert ! video/x-raw, format=BGR ! appsink", cv2.CAP_GSTREAMER)
        #cam = cv2.VideoCapture(0)
    if (delay):
        time.sleep(delay)         

    ret,frame = cam.read()
    print(ret)
    print(frame)
    s = generateImageName()
    cv2.imwrite(s, frame)


def saveImage(img, name):
    s = generateImageName(name)
    cv2.imwrite(s, img)

    return s


if __name__ == "__main__":
    print("Capturing Photo in 5 seconds.")

    captureImage(delay=5, capture_width=480, capture_height=480)

