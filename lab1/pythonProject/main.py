
import cv2
import numpy as np
from math import ceil
import os

dst = "./img/"
images = os.listdir(dst)
length = len(images)
result = np.zeros((360,360,3), np.uint8)
i = 1

a = 1.0
b = 0.0
img = cv2.imread(dst + images[i])
img = cv2.resize(img, (360, 360))
stop = True
temp=5
while(True):

    if i == length-1:
        i=1
    if(ceil(a)==0):
        a = 1.0
        b = 0.0
        if stop == False:
            i = (i+1)%length
        img = cv2.imread(dst + 'photo'+str(i)+'.png')
        img = cv2.resize(img, (360, 360))

    a -= 0.01
    b += 0.01
    result = cv2.addWeighted(result, a, img, b, 0)
    cv2.imshow("Slajdy", result)
    key = cv2.waitKey(temp) & 0xff
    if key==ord('q'):
        break
    if key==ord('a'):
        stop = False
    if key == ord('w'):
        i=i+1
    if key == ord('e'):
        i=i-1
    if key==ord('z'):
        temp=temp+5
    if key == ord('x'):
        if temp !=5:
            temp=temp-5
cv2.destroyAllWindows()