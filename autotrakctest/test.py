import cv2
import numpy
from matplotlib import pyplot as plt


def preprocess_image(image):
    
    bilateral_filtered_image = cv2.bilateralFilter(image, 7, 150, 150)
    
    gray_image = cv2.cvtColor(bilateral_filtered_image, cv2.COLOR_BGR2GRAY)
    return gray_image

img1 = cv2.imread('./data/cell1.jpg')
img2 = cv2.imread('./data/cell2.jpg')
img1 = img1[800:1800,500:900]
img2 = img2[800:1800,500:900]

preprocess_image1 = preprocess_image(img1)
preprocess_image2 = preprocess_image(img2)

diff = cv2.absdiff(preprocess_image1, preprocess_image2)

kernel = numpy.ones((5,5),numpy.uint8)

close_operated_image = cv2.morphologyEx(diff, cv2.MORPH_CLOSE, kernel)
cv2.imshow('3',close_operated_image)


_, thresholded = cv2.threshold(close_operated_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('2',thresholded)

median = cv2.medianBlur(thresholded, 5)
contours,_ = cv2.findContours(median, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img1, contours, -1, (100, 0, 255),2)

# angle = cv2.fitEllipse(contours)

plt.subplot(1,2,1)
plt.imshow(img1)
plt.subplot(1,2,2)    


plt.imshow(img2)
plt.show()
