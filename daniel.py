import glob

image = 'C:\\Users\\daste19\\Desktop\\projects\\flood_pred\\total_frames\\videosframe2436.png'
# a = image[10:-4]
# print(a)


def order(x):
    y = x[69:-4]
    return int(y)


print(order(image))
images = glob.glob("C:\\Users\\daste19\\Desktop\\projects\\flood_pred\\total_frames\\*")



for image in sorted(images, key=order):
    print(image)