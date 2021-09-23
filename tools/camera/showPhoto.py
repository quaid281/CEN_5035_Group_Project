#!/usr/bin/python2

import cv2

image_path = "/home/rob/work/camera/foo.jpg"

img = cv2.imread(image_path)

cv2.imshow("show", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
