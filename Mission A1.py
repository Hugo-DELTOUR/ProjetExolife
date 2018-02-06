import cv2
import numpy as np

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/Encelade_surface.pbm', 0)

isize = img.shape
print (isize)
maxi= 0
coord = []
for i in range (0 , isize[0]):
    for j in range (0, isize[1]):
        if img[i][j] >= maxi:
            maxi = img[i][j]
            coord = [i,j]

print(coord)

cv2.circle(img, (coord[0], coord[1]), 10, (255,255,255), 1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()