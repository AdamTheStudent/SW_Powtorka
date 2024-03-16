import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('dokument.jpg')
image = cv2.resize(image, None, fx=0.5, fy=0.5)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image,(5,5),0)
image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
#
cv2.imwrite('dokument_out_1.jpg', image)
pts1 = np.float32([[0, 585], [1555, 510], [0, 1930], [1555, 1750]])
height, width = image.shape[:2]
pts2 = np.float32([[0, 0], [width, 0], [0,height], [width, height]])

M = cv2.getPerspectiveTransform(pts1, pts2)

image = cv2.warpPerspective(image, M, (width, height))

# plt.imshow(image), plt.title('Obraz')
# plt.show()
cv2.imwrite('dokument_out_2.jpg', image)


