import cv2
import numpy as np


def empty_callback(value):
    pass

# create a black image, a window
img = np.zeros((300, 500, 3), dtype=np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, empty_callback)
cv2.createTrackbar('G', 'image', 0, 255, empty_callback)
cv2.createTrackbar('B', 'image', 0, 255, empty_callback)
dog = cv2.imread('dog.jpg')
dog = cv2.resize(dog, (500, 360))
# create switch for ON/OFF functionality
#switch_trackbar_name = '0 : OFF \n1 : ON'
#cv2.createTrackbar(switch_trackbar_name, 'image', 0, 1, empty_callback)
#print(dog.shape[0])
polowa_szer=int(dog.shape[0]/2)
polowa_dl=int(dog.shape[1]/2)
maskR = cv2.inRange(img, (0, 0, 0), (255, 0, 0))
while True:
    cv2.imshow('image', dog)

    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break
    # get current positions of four trackbars
    r_th = cv2.getTrackbarPos('R', 'image')
    g_th = cv2.getTrackbarPos('G', 'image')
    b_th = cv2.getTrackbarPos('B', 'image')

    firstQ =dog[0:polowa_szer,0:polowa_dl]
    secondQ=dog[0:polowa_szer,polowa_dl:dog.shape[1]]
    thirdQ=dog[polowa_szer:dog.shape[0],0:polowa_dl]
    fourthQ=dog[polowa_szer:dog.shape[0],polowa_dl:dog.shape[1]]
    gray=cv2.cvtColor(firstQ, cv2.COLOR_BGR2GRAY)
    b = fourthQ.copy()
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    th1,b=cv2.threshold(b,b_th,255,cv2.THRESH_BINARY)

    g = thirdQ.copy()

    g[:, :, 0] = 0
    g[:, :, 2] = 0
    th2,g = cv2.threshold(g, g_th, 255, cv2.THRESH_BINARY)
    r = secondQ.copy()
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    th3,r = cv2.threshold(r, r_th, 255, cv2.THRESH_BINARY)
    imgc = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    a =np.concatenate((imgc,r),axis=1)
    beka =np.concatenate((g,b),axis=1)
    wynik=np.concatenate((a,beka),axis=0)
    cv2.imshow('wynik', wynik)


    wynikOSTfirstQ=imgc
    r[:, :, 0]=secondQ[:,:,0]
    r[:, :, 1] = secondQ[:,:,1]
    wynikOSTsecondQ=r
    g[:, :, 0]=thirdQ[:,:,0]
    g[:, :, 2] = thirdQ[:,:,2]
    wynikOSTthirdQ = g
    b[:, :, 1]= fourthQ[:,:,1]
    b[:, :, 2] = fourthQ[:,:,2]
    wynikOSTfourthQ = b
    ale =np.concatenate((wynikOSTfirstQ,wynikOSTsecondQ),axis=1)
    ba =np.concatenate((wynikOSTthirdQ,wynikOSTfourthQ),axis=1)
    Powrot = np.concatenate((ale, ba), axis=0)
    cv2.imshow('Po progowaniu kanalow', Powrot)
cv2.destroyAllWindows()
