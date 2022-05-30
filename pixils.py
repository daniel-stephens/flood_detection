import numpy as np
import cv2
import glob
import os
import pandas as pd
import plotly.express as px

images = sorted(glob.glob(f"{os.getcwd()}\\background\\*jpg"), key=len)
roi = (40, 5, 180, 159)

pixils = []
frame_number = []
n = 0

for image in images:
    img_raw = cv2.imread(image)
    #Crop selected roi from raw image
    roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    num = np.sum(roi_cropped)
    pixils.append(num)
    frame_number.append(n)
    n+=1
df = pd.DataFrame({'frame_number': frame_number,
                    'pixils': pixils})

print(df.head())








# #select ROI function
# roi = cv2.selectROI(img_raw)

# #print rectangle points of selected roi

# #Crop selected roi from raw image
# roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

# print(roi)
# num = np.sum(roi_cropped)
# print(num)
# #show cropped image
# # cv2.imshow("ROI", roi_cropped)

# # cv2.imwrite("crop.jpeg",roi_cropped)

# #hold window
# cv2.waitKey(0)