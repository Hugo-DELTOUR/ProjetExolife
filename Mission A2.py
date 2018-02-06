import cv2
import numpy as np

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/Mars_surface.pbm', 0)

isize = img.shape
maxi = 0
coord = []
for i in range (0 , isize[0]):
    for j in range (0, isize[1]):
            maxi += img[i][j]

print((maxi/255)/((i+1)*(j+1)))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()