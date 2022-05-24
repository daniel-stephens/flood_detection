import cv2
import numpy as np
import glob
import os


images = sorted(glob.glob(f"{os.getcwd()}\\averaged\\*jpg"), key=len)
initial_image = cv2.imread(images[0]).astype(np.float16)
n = 0
for image in images:
    im = cv2.imread(image).astype(np.float16)
    diff = abs(initial_image - im)
    diff = np.where(diff>90, 225, 0).astype(np.uint8)

    output = ".\\background\\image{}.jpg".format(n)
    print("Image {} done!!!!!!!!!".format(n))
    cv2.imwrite(output, diff)
    n +=1



# img1 = cv2.imread('.\\averaged\\averaged0.jpg').astype(np.float16)
# img2 = cv2.imread('.\\averaged\\averaged6000.jpg').astype(np.float16)

# diff = abs(img1 - img2)
# diff = np.where(diff>100, 225, 0)

# diff = diff.astype(np.uint8)


# imga1 = cv2.imread('.\\averaged\\averaged0.jpg')
# imga2 = cv2.imread('.\\averaged\\averaged6000.jpg')
# cv2.imshow('output', diff)
# cv2.imshow('image1', imga1)
# cv2.imshow('Image2', imga2)

# cv2.waitKey(0) 