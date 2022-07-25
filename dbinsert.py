import os
import cv2
import glob
import numpy as np
import sqlite3
import time



con = sqlite3.connect('database.db')
cur = con.cursor()

images = sorted(glob.glob(f"{os.getcwd()}\\background\\*jpg"), key=len)
roi = (40, 5, 180, 159)
n = 0

for image in images:
    img_raw = cv2.imread(image)

    #Crop selected roi from raw image
    roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    num = np.sum(roi_cropped)
    # print(num)
    query = "INSERT INTO vid_pixils (frame_number, pixils, image) VALUES({}, {}, {})".format(n, num, str(image))
    # c.execute('''INSERT INTO site VALUES(NULL, "meh","lang",?,"RSS","argh")''', rss_link)

    # Insert a row of data
    cur.execute('''INSERT INTO vid_pixils  (frame_number, pixils, images) VALUES(?, ?, ?)''',( n, str(num), image))

    print('Data Successfully Inserted Into the Database')
    # Save (commit) the changes
    con.commit()
    n+=1
    time.sleep(0.1)


con.close()