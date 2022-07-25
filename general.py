import cv2
import glob
import os


images = sorted(glob.glob(".\\total_frames\\*.png"), key=len)
im = cv2.imread(images[0])
roi = cv2.selectROI(im)
n = 0
for image in images:
    im = cv2.imread(image)
    cropped_image = im[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    # name = '.\\roi\\cropped'+str(n)+".png"
    # cv2.imwrite(name, cropped_image)
    print(str(n)+" number of images completed")
    if n == 50000:
        break
    print(n)
    n+=1
