import cv2
from pytesseract import pytesseract
import glob
import numpy as np
import os
from pymongo import MongoClient


cluster = "mongodb://localhost:27017"
client = MongoClient(cluster)
print(client.list_database_names())
db = client.FloodDetection


pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
images = sorted(glob.glob(f"{os.getcwd()}\\total_frames\*.png"), key=len)
im = cv2.imread(images[0])
roi = cv2.selectROI(im)
n = 0
cv2.destroyAllWindows()
for image in images:
    im = cv2.imread(image)
    f_date = im[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    # b = np.where(f_date>240, 250, 0)
    date = pytesseract.image_to_string(f_date)[:8]
    reu1 = {
        "frame number": n, 
        "time": date,
        "path": image
        }
    reu = db.general
    reu.insert_one(reu1)
    print(n)
    if n == 50000:
        break
    n+=1
    
