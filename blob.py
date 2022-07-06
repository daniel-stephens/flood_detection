
import cv2
import numpy as np

kernel1 = np.ones((1, 2), np.uint8)
kernel2 = np.ones((2, 2), np.uint8)
image = cv2.imread('.\\background\\image46091.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (6, 5))

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
# cv2.connectedComponentsWithStats
# img = cv2.erode(image, kernel, iterations=3)

# img2 = cv2.dilate(img, kernel, iterations=8)

# im = image.astype(np.float16)


# cv2.imshow('Erosion', img)
cv2.imshow('closing', closing)
# cv2.imshow('Output', image)
cv2.waitKey(0)


# apply connected component analysis to the thresholded image
output = cv2.connectedComponentsWithStats(closing, 3, cv2.CV_32S)
(numLabels, labels, stats, centroids) = output

print(output)