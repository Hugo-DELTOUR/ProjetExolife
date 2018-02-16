import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/Gliese 667Cc_surface.pbm', 0)

isize = img.shape

histo = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram')

equ = cv2.equalizeHist(img)

histo = cv2.calcHist([equ],[0],None,[256],[0,256])
plt.hist(equ.ravel(),256,[0,256])
plt.title('Histogram')

plt.show()

cv2.imshow('equalize',equ)
cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()