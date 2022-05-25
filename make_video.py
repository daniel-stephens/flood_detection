import cv2
import os
import glob

def frames_to_video(frames_path, output_path):
    images = sorted(glob.glob(f'{os.getcwd()}{frames_path}'), key=len )
    

    # This block of code gets the dimensions of the image and appends the images to a list
    frame_array =[]
    for i in range(len(images)):
        image  = images[i]
        img = cv2.imread(image)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

    # This block of code takes the list of images and the size, and makes a video from it
    out = cv2.VideoWriter(output_path, -1, 30, size) 

    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

if __name__=="__main__":
    frames_path = ".\\background\\*.jpg"
    output = ".\\videos\\background.mp4"

    frames_to_video(frames_path, output)
