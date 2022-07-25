import glob
import cv2
import os
import numpy as np

images_total = sorted(glob.glob(f"{os.getcwd()}\\roi\\*png"), key=len)

# We are going to average 50 videos at a time to clear the noise

first = 30
n = 0
while first<50000:
    images = images_total[first-30:first]
    image_data=[]
    for image in images:
        im = cv2.imread(image)
        image_data.append(im)
        avg_image=image_data[0]

        for i in range(len(image_data)):
            if i ==0:
                pass
            else:
                alpha = 1.0/(i+1)
                beta = 1.0 - alpha
                avg_image = cv2.addWeighted(image_data[i], alpha, avg_image, beta, 0.0)
    name = ".\\averaged\\averaged{}.jpg".format(n)
    cv2.imwrite(name, avg_image)
    n+=1
    first +=1

    print("The average image {} is done".format(n))

