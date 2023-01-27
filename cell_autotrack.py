import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./data/tank2.jpg',0)
img2 = cv2.imread('./data/tank.jpg',0)


SobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
SobelY = cv2.Sobel(img,cv2.CV_64F,0,1)

SobelX = np.uint8(np.absolute(SobelX))
SobelY = np.uint8(np.absolute(SobelY))

SobelCombined = cv2.bitwise_or(SobelX,SobelY)


SobelX2 = cv2.Sobel(img2,cv2.CV_64F,1,0)
SobelY2 = cv2.Sobel(img2,cv2.CV_64F,0,1)

SobelX2 = np.uint8(np.absolute(SobelX))
SobelY2 = np.uint8(np.absolute(SobelY))

SobelCombined2 = cv2.bitwise_or(SobelX,SobelY)

titles = ['before','after']
images = [SobelCombined,SobelCombined2]

diff = cv2.absdiff(img,img2)

for i in range(len(titles)):
    plt.subplot(2,1,i+1), 
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()