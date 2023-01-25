import cv2
import numpy as np 

# events = [i for i in dir(cv2)]
# print(events)

def click_event(event,x,y,flags,param):
    font = cv2.FONT_HERSHEY_COMPLEX
    
    # show position
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        
        XY_coord = str(x) + ', '+ str(y)
        cv2.putText(img,XY_coord,(x,y),font,.5,(255,0,255),2)
        cv2.imshow('Left_Click',img)
   
    # Show color 
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        strBGR = str(blue) + '， ' + str(green)+ ', ' + str(red)
        cv2.putText(img, strBGR,(x,y),font,0.5,(255,2,2),2)
        cv2.imshow('Right-Click',img)
    
def draw_points(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(0,0,255),-1)
        points.append((x,y))
        if len(points) >=2:
            cv2.line(img,points[-1],points[-2],[255,5,5],3)
        cv2.imshow('image',img)

def pixel_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        
        Color_Image = np.zeros((512,512,3),np.uint8)
        # fill the color
        Color_Image[:] = [blue,green,red]
        cv2.imshow('color',Color_Image)
    
img = cv2.imread('./Handle_MouseEvent/lena.jpg')

# img = np.zeros((512,512,3),np.uint8)
points =[]
cv2.imshow('image',img)

cv2.setMouseCallback('image',pixel_color)
# cv2.setMouseCallback('image',draw_points)

cv2.waitKey(0)
cv2.destroyAllWindows()