import numpy as np
import cv2
import glob
import os
import pandas as pd
import plotly.express as px










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