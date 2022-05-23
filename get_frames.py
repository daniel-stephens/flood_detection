import cv2

# Function to get frames from video
def get_frames(input_path, output_path):
    
    video = cv2.VideoCapture(input_path)
    currentframe = 0

    while (True):
        ret, frame = video.read()
        
        if ret:
            name = output_path + 'videosframe'+str(currentframe)+".png"
            print('Captured...' + name)
            cv2.imwrite(name, frame)
              
            if currentframe == 50000:
                break
            currentframe +=1

        else:
            break

if __name__ == '__main__':
    
    input_path = '.\\Videos\\Ellicott City 2018 Flood Multicam  REVISED.mp4'

    output_path = ".\\total_frames\\"
    
    get_frames(input_path, output_path)