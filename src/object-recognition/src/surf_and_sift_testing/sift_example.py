import cv2
import numpy as np
import time

print cv2.__version__

image = cv2.imread('enclosure.jpg')
surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(image, None)
print des.shape
print len(kp)
print surf.hessianThreshold
print surf.upright
print surf.descriptorSize()

image = cv2.drawKeypoints(image, kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('surf_test3.jpg', image)
