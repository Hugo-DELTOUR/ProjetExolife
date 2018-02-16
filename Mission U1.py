import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/U1_surface.pbm',0)

imgsize = img.shape

histo = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram')

plt.subplot(161)
plt.imshow(img, cmap = 'gray')
plt.title('Input Img')

equa = cv2.equalizeHist(img)

plt.subplot(162)
plt.imshow(equa, cmap = 'gray')
plt.title('Equalize')

kernelx = np.array([[1,0],[0,-1]])
kernely = np.array([[0,1],[-1,0]])


imgRobertsx = cv2.filter2D(img,-1,kernelx)
imgRobertsy = cv2.filter2D(img,-1,kernely)
imgRoberts = imgRobertsy+imgRobertsx
imgRobertsNorm = cv2.equalizeHist(imgRoberts)

imgRobertsThresh = copy.copy(imgRoberts)

for i in range (0, imgsize[0]):
    for j in range (0, imgsize[1]):
        if imgRoberts[i][j] > 27:
            imgRobertsThresh[i][j] = 255
        else :
            imgRobertsThresh[i][j] = 0

plt.subplot(163)
plt.imshow(imgRobertsx, cmap = 'gray')
plt.title('RobertsX')

plt.subplot(164)
plt.imshow(imgRobertsy, cmap = 'gray')
plt.title('RobertsY')

plt.subplot(165)
plt.imshow(imgRoberts, cmap = 'gray')
plt.title('Roberts')

plt.subplot(165)
plt.imshow(imgRobertsNorm, cmap = 'gray')
plt.title('Roberts Equalized')

plt.subplot(166)
plt.imshow(imgRobertsThresh, cmap = 'gray')
plt.title('Roberts Thresh')

plt.show()