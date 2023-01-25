import cv2 
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('./data/tank.jpg',0)

# laplacian
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

# Sobel
SobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
SobelY = cv2.Sobel(img,cv2.CV_64F,0,1)

SobelX = np.uint8(np.absolute(SobelX))
SobelY = np.uint8(np.absolute(SobelY))

SobelCombined = cv2.bitwise_or(SobelX,SobelY)
canny = cv2.Canny(img, 100, 200)

titles = ['image','laplacian','SobelX','SobelY','SobelCombined','canny']
images = [img,lap,SobelX,SobelY,SobelCombined,canny]


for i in range(len(titles)):
    plt.subplot(2,3,i+1), 
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()