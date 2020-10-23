import cv2
import os

if not os.path.exists('gopro_vids'):
    os.makedirs('gopro_vids')
for filename in os.listdir('Recycle'):
    if filename.startswith('.'):
        continue
    if not os.path.exists('gopro_vids/' + str(filename)):
        os.makedirs('gopro_vids' + str(filename))
    vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
    success,image = vidcap.read()
    count = 0
    while success:
        if (count%5 == 0):
            cv2.imwrite("gopro_vids/" + str(filename) + "/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1