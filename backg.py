import cv2
from cv2 import cvtColor
import numpy as np
import glob



img1 = cv2.imread('.\\averaged\\averaged0.jpg')
img2 = cv2.imread('.\\averaged\\averaged15000.jpg')

# diff = abs(img1 - img2)
# diff = np.where(diff>100, 225, 0)

# diff = diff.astype(np.uint8)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sub = cv2.subtract(gray2, gray1)
ret, th = cv2.threshold(sub, 70, 255, cv2.THRESH_BINARY)




imga1 = cv2.imread('.\\averaged\\averaged0.jpg')
imga2 = cv2.imread('.\\averaged\\averaged15000.jpg')
cv2.imshow('output', th)
cv2.imshow('image1', gray1)
cv2.imshow('Image2', gray2)
cv2.imshow('outp', sub)

cv2.waitKey(0)