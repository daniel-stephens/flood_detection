import cv2
import glob
import os



def roi_crop(image_path):
    images = sorted(glob.glob(image_path+'*.png'), key=len)

    im = cv2.imread(images[0])
    roi = cv2.selectROI(im)
    print(roi[0])
    return roi



if __name__ == '__main__':



    folder= ".\\total_frames\\"
    roi_crop(folder)
#images = sorted(glob.glob(folder+'*.png'), key=len)
# for i in images:
#     print(i)


