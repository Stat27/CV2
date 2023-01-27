import cv2 
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('./data/tank.jpg',0)
canny = cv2.Canny(img, 100, 200)

titles = ['image','canny']
images = [img,canny]

plt.imshow(images[1],'gray')
plt.title(titles[1])
plt.xticks([]), plt.yticks([])

plt.show()