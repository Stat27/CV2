import numpy as np 
import cv2

img = cv2.imread('./basic_operation_image/left01.jpg')

print(img.shape) # rows,colums ...
print(img.size) # total pixels
print(img.dtype) # datatype

# b,g,r = cv2.split(img)

# img = cv2.merge((b,g,r))
apple = img[100:150,200:300]
img[200:250,100:200] =apple



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
