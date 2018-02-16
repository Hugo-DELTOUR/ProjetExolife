import imutils
import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/U2_surface.pbm')

histo = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram')

plt.show()

image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(image,200,300)

cont = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cont = cont[0] if imutils.is_cv2() else cont[1]

cont = sorted(cont, key = cv2.contourArea, reverse = True)[:10]

cv2.drawContours(img, cont, 0, (0,255,0), -1)

cv2.imshow('Canny',canny)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()