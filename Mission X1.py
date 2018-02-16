import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/delto/Desktop/IMAGE exolife/deathStar.pbm',0)

histo = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram')

fourier = np.fft.fft2(img)
fshift = np.fft.fftshift(fourier)
magnitude_spectre = 20*np.log(np.abs(fshift))

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131)
plt.imshow(img, cmap = 'gray')
plt.title('Input Img')

plt.subplot(132)
plt.imshow(magnitude_spectre, cmap='gray')
plt.title('Magnitude Spectre')

plt.subplot(133)
plt.imshow(img_back, cmap='gray')
plt.title('Result after HPF')

plt.show()