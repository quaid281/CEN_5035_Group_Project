#!/usr/bin/python2

import cv2

"""
Thanks to github.com/JetsonHacksNano/CSI-Camera/blob/master/simple_camera.py
for having parameters available for using the Raspberry Pi Camera V2
that are useful for video capture.
"""
def nano_cam_params(
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
        
             
cam = cv2.VideoCapture(nano_cam_params(), cv2.CAP_GSTREAMER)

ret,frame = cam.read()
cv2.imshow("preview", frame)
cv2.waitKey(0)
cv2.imwrite("foo.jpg", frame)
