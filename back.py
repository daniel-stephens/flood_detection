import cv2
import numpy as np

kernel1 = np.ones((1, 2), np.uint8)
kernel2 = np.ones((2, 2), np.uint8)

imgg = cv2.imread('.\\averaged\\averaged42091.jpg')
image1 = imgg.astype(np.float16)
image2 = cv2.imread('.\\averaged\\averaged0.jpg').astype(np.float16)

diff = abs(image1 - image2)
diff = np.where(diff>120, 255, 0).astype(np.uint8)
#img = cv2.erode(diff, kernel1, iterations=2)
#img2 = cv2.dilate(img, kernel2, iterations=3)

cv2.imwrite('frame42091.jpg', diff)



cv2.imshow('img', imgg)
cv2.imshow('img2', diff)

cv2.waitKey(0)