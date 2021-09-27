#!/usr/bin/python

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

def captureImage(delay=0, capture_width=1920, capture_height=1080):

    cam = cv2.VideoCapture(sci_cam_params(capture_width, capture_height), cv2.CAP_GSTREAMER)
       
    if (delay):
        time.sleep(delay)         

    ret,frame = cam.read()
    s = generateImageName()
    cv2.imwrite(s, frame)


if __name__ == "__main__":
    print("Capturing Photo in 5 seconds.")

    captureImage(5, capture_width=480, capture_height=480)
