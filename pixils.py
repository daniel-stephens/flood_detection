import numpy as np
import cv2
img_raw = cv2.imread('.\\background\\image4091.jpg')




#select ROI function
roi = cv2.selectROI(img_raw)

#print rectangle points of selected roi
print(roi)

#Crop selected roi from raw image
roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

# num = np.sum(roi_cropped)
for row in range(img_raw.shape[0]):
    for column in range(img_raw.shape[1]):
        if roi_cropped[row, column] <100:
            roi_cropped[row, column]=0

print(num)
#show cropped image
cv2.imshow("ROI", roi_cropped)

# cv2.imwrite("crop.jpeg",roi_cropped)

#hold window
cv2.waitKey(0)