import glob
import numpy as np
import cv2
from matplotlib import image, pyplot as plt
from pymongo import MongoClient
import time
import os

cluster = "mongodb://localhost:27017"
client = MongoClient(cluster)
print(client.list_database_names())
db = client.FloodDetection
print(db.list_collection_names())

# import all image files with the .jpg extension
def order(x):
    y = x[58: -4]
    return int(y)

images = sorted(glob.glob(f"{os.getcwd()}\\roi\\*png"), key=len)

frameNR=0
first = True
for w in range(len(images)):
    if w == 0:
        pass
    else: 
        image_set = images[w:w+30]
        e_list = []
        for m in image_set:
            e_list.append(cv2.imread(m))

        avg_image = e_list[0]
        for w in range(len(image_set)):
            if w ==0:
                pass
            else:
                alpha = 1.0/(w+1)
                beta = 1.0 -alpha
                avg_image = cv2.addWeighted (e_list[w], alpha, avg_image, beta, 0.0)
        # cv2.imwrite(f'/Users/wilson006/Desktop/Vscode/Cleaner_Image/{name}.jpg', avg_image)
        if first == True:
            first_frame = avg_image
            first = False
        image = avg_image
        gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
        graytwo = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sub = cv2.subtract(graytwo, gray)
        #Morph
        ret, th = cv2.threshold(sub, 80, 255, cv2.THRESH_BINARY)
        kernel = np.ones((2,2), np.uint8)
        dilation = cv2.dilate(th, kernel, iterations = 1)
        #Pixels
        number_of_white_pix = np.sum(dilation)
        print('Number of white pixels:', number_of_white_pix)
        reu1 = {"frame number": frameNR, "number of pixel": int(number_of_white_pix)}
        reu = db.pixils
        reu.insert_one(reu1)
        frameNR= frameNR+1
        time.sleep(0.01)
print("Yeah Boy")