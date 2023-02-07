import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./data/cell1.jpg')
img2 = cv2.imread('./data/cell2.jpg')

img = img[800:1800,500:900]
img2 = img2[800:1800,500:900]


diff = cv2.absdiff(img,img2)
gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    
    # for clean differences
blur = cv2.GaussianBlur(gray,(5,5),0)

_,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
dilated = cv2.dilate(thresh,None, iterations=3)

contours, hierrachy = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# draw rectangle around contour
for contour in contours:
    # find x,y,width,height
    (x,y,w,h) = cv2.boundingRect(contour)
        
    # if cv2.contourArea(contour)<800:
    #     continue
    print(w,h)
    cv2.rectangle(img,(x,y), (x+w,+y+h),(0,255,0),2)
    cv2.putText(img,'status:{}'.format("Movement"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,2,2),3)
    # cv2.drawContours(img,contours,-1,(255,0,255),2)
    # cv2.imshow('feed',img2)

plt.subplot(1,2,1)
plt.imshow(img,'gray')
plt.subplot(1,2,2)    


plt.imshow(img2,'gray')
plt.title('Movement')


plt.show()
