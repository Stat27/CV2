import datetime
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./open_video/output.avi',fourcc,20, (640,480))

# The height and width are limited to the original camera resolution
# set height
# cap.set(3,3000)

# #set width
# cap.set(4,2000)


# while True:
#     ret, frame = cap.read()
    
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (cap.isOpened()):
    ret, frame = cap.read()
    
    # ret means if the frame is available
    if ret == True:
        
        
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame,datet,(10,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0),1,cv2.LINE_4)
        
        out.write(frame)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
out.release()
