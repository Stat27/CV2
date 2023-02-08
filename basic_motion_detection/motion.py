import cv2
import numpy as np

cap = cv2.VideoCapture('./data/vtest.avi')

ret,frame1 = cap.read()
ret,frame2 = cap.read()

while cap.isOpened():
    # find difference
    diff = cv2.absdiff(frame1,frame2)
    
    # clear noises
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    
    # for clean differences
    blur = cv2.GaussianBlur(gray,(5,5),0)
    
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None, iterations=3)
    
    contours, hierrachy = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame2,contours,-1,(0,255,0),1)
    # draw rectangle around contour
    for contour in contours:
        # find x,y,width,height
        (x,y,w,h) = cv2.boundingRect(contour)
        
        if cv2.contourArea(contour)<900:
            continue
        
        cv2.rectangle(frame1,(x,y), (x+w,+y+h),(0,255,0),2)
        cv2.putText(frame1,'status:{}'.format("Movement"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,2,2),3)
    # cv2.drawContours(frame1,contours,-1,(255,0,255),2)
    cv2.imshow('feed',frame1)
    cv2.waitKey(0)
    frame1 = frame2
    ret,frame2 = cap.read()
    
    
    if cv2.waitKey(40) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()