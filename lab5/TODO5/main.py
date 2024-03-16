import cv2 as cv
import numpy as np


def zad2():
    # Use a breakpoint in the code line below to debug your script.
    img = cv.imread('fruit.jpg', cv.IMREAD_GRAYSCALE)
    img = cv.medianBlur(img, 5)
    cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 80,
                              param1=30, param2=90, minRadius=40, maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        color = cimg[i[1], i[0]]
        print(color)
        if color[0] < 100:
            cv.circle(cimg, (i[0], i[1]), i[2], (0, 0, 255), 2)
            #print()

        else:
            cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 255), 2)

        # draw the center of the circle
        cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv.imshow('detected circles', cimg)
    cv.waitKey(0)
    cv.destroyAllWindows()  # Press Ctrl+F8 to toggle the breakpoint.


def zad1():
    img = cv.imread(cv.samples.findFile('drone_ship.jpg'))  # , cv.IMREAD_GRAYSCALE)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 250, 255, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1.5, np.pi / 180, 100, minLineLength=70, maxLineGap=5)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv.imshow('detected circles', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def zad3():
    img = cv.imread('coins.jpg', cv.IMREAD_GRAYSCALE)
    img = cv.medianBlur(img, 13)
    cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1.5, 160,
                              param1=80, param2=50, minRadius=25, maxRadius=130)

    circles = np.uint16(np.around(circles))
    pieniadze=0
    for i in circles[0, :]:
        # draw the outer circle
        cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)

        if i[2]>100:
            pieniadze=pieniadze+100
        elif i[2]<55:
            pieniadze=pieniadze+10

        # draw the center of the circle
        cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    print((pieniadze/100),"zl")
    # cv.imshow('detected circles', cimg)
    # cv.waitKey(0)
    # cv.destroyAllWindows()  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    # zad1()
    # zad2()
    zad3()
