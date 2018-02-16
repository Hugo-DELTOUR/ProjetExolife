import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/Gliese 581d V2.pbm',0)

histo = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram')

median1 = cv2.medianBlur(img,5)
median2 = cv2.medianBlur(median1,5)

plt.subplot(131)
plt.imshow(img, cmap = 'gray')
plt.title('Input Img')

plt.subplot(132)
plt.imshow(median1, cmap = 'gray')
plt.title('Median Blur1')

plt.subplot(133)
plt.imshow(median2, cmap = 'gray')
plt.title('Median Blur2')

plt.show()