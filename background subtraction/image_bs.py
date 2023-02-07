import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt 

img = cv.imread('./data/tank.jpg')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()

#fgbg = cv.bgsegm.BackgroundSubtractorGMG()
#fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=True)
#fgbg = cv.createBackgroundSubtractorKNN(detectShadows=True)

fgmask = fgbg.apply(img)
#fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)

# cv.imshow('Frame', img)
# cv.imshow('FG MASK Frame', fgmask)

plt.subplot(2,1,1)
plt.imshow(img)
plt.subplot(2,1,2)
plt.imshow(fgmask)

plt.show()

keyboard = cv.waitKey(0)
if keyboard == 'q' or keyboard == 27:
    cv.destroyAllWindows()