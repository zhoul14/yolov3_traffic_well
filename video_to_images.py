import cv2
import sys
import os
filename = sys.argv[1]
dirname = str(filename).split('.')[0]+'/'
print(dirname)

if sys.argv.__len__() >2:
    dirname = sys.argv[2]

print(dirname)

if os.path.exists(dirname) == False:
    print("mkdir:%s"%dirname)
    os.makedirs(dirname)

vidcap = cv2.VideoCapture(filename)
success,image = vidcap.read()
count = 0
success = True
while success:
    success,image = vidcap.read()
    cv2.imwrite("1016-1020/frame%.5d.jpg" % count, image)     # save frame as JPEG file
    if cv2.waitKey(1) == 27:
        break
    count += 1
