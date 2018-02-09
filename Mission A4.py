import cv2
import numpy as np

jupiter1 = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/Jupiter1.pbm', 0)
jupiter2 = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/Jupiter2.pbm', 0)

isize=jupiter1.shape

jupiter3 = cv2.addWeighted(jupiter1,0.5,jupiter2,0.5,0)

jupiter3 = cv2.medianBlur(jupiter3,5)

cv2.imshow('image1',jupiter1)
cv2.imshow('image2',jupiter2)
cv2.imshow('image', jupiter3)
cv2.waitKey(0)
cv2.destroyAllWindows()