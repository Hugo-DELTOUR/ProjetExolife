import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/GD61.pbm', 0)

isize = img.shape
cv2.imshow('Image',img)

histo = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram')

plt.show()

norm = cv2.normalize(img,img,255,255,1)
cv2.imshow('Normalize', norm)

cv2.waitKey(0)
cv2.destroyAllWindows()