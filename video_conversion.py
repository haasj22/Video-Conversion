import cv2
import os

if not os.path.exists('gopro_vids'):
    os.makedirs('gopro_vids')
for filename in os.listdir('Recycle'):
    if filename.startswith('.'):
        continue
    if not os.path.exists('gopro_vids/' + str(filename)[:-4]):
        os.makedirs('gopro_vids/' + str(filename)[:-4])
    vidcap = cv2.VideoCapture("Recycle/" + str(filename))
    success,image = vidcap.read()
    count = 0
    while success:
        print(count)
        cv2.imwrite("gopro_vids/" + str(filename)[:-4] + "/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1