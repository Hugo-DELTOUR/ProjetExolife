import cv2
import numpy as np

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/Europa_surface.pbm', 0)

ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('image', img)
cv2.imshow('thershold',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
