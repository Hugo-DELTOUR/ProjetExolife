import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/HD215497.pbm')
img1 = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/HD215497.pbm',0)

#histo = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.hist(img.ravel(),256,[0,256])
#plt.title('Histogram')

#plt.show()

isize = img.shape

for i in range (0 , isize[0]):
    for j in range (0, isize[1]):

        if img1[i][j] >= 192:
           img[i][j] = [0,255,255]

        if img1[i][j] < 192:
            img[i][j] = [0, 0, 255]

        if img1[i][j] < 128:
            img[i][j] = [0, 255, 0]

        if img1[i][j] < 64:
            img[i][j] = [0, 0, 0]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
