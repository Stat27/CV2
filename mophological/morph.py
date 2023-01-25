import cv2
from matplotlib import pyplot as plt 
import numpy as np 

img = cv2.imread('./data/smarties.png',0)

_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2),np.uint8)

dilation = cv2.dilate(mask,kernal,iterations=3)
erosion = cv2.erode(mask,kernal,iterations=1)

titles = ['images','mask','dilation','erosion']
images = [img,mask,dilation,erosion]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
