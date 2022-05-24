
import cv2
import numpy as np

kernel1 = np.ones((1, 2), np.uint8)
kernel2 = np.ones((2, 1), np.uint8)
image = cv2.imread('.\\background\\image4091.jpg')

img = cv2.erode(image, kernel1, iterations=2)

img2 = cv2.dilate(img, kernel2, iterations=5)

im = image.astype(np.float16)

cv2.imshow('Erosion', img)
cv2.imshow('Dialation', img2)
cv2.imshow('Output', image)
cv2.waitKey(0)