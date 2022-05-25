
import cv2
import numpy as np

kernel1 = np.ones((1, 2), np.uint8)
kernel2 = np.ones((2, 2), np.uint8)
image = cv2.imread('.\\background\\image4091.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))


img = cv2.erode(image, kernel, iterations=3)

img2 = cv2.dilate(img, kernel, iterations=8)

im = image.astype(np.float16)


cv2.imshow('Erosion', img)
cv2.imshow('Dialation', img2)
cv2.imshow('Output', image)
cv2.waitKey(0)