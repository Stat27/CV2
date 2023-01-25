import cv2
import numpy as np

# [height,weidth,3]
img = np.zeros([512,512,3],np.uint8)
# img = cv2.imread('./cv2open/lena.jpg', 1)
print(img)

img = cv2.line(img,(0,0),(255,255),(147,99,44),10)
img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),10)

img = cv2.rectangle(img, (284,0),(510,128),(0,0,255),-1)
img = cv2.circle(img, (447,63),20, (1,2,3),-1)

img = cv2.putText(img,'Drawing_Practices', (10,500),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,255),10,cv2.LINE_4)

cv2.imshow('image',img)
cv2.imwrite('./draw_geometric_image/mypic.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()