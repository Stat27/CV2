import numpy as np 
import cv2
from tkinter.filedialog import askdirectory
import os

folder = askdirectory()
All_images = []
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# fgbg = cv2.bgsegm.BackgroundSubtractorGMG()
# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)
for path, subdirs, files in os.walk(folder,topdown=True):
    # iterates over every file in the selected directory
    for filename in files:
        src = os.path.join(path,filename)
        img = cv2.imread(src)
        All_images.append(img)
        


cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Frame", 2448, 2080)

cv2.namedWindow("FG MASK Frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow("FG MASK Frame", 2448, 2080)
for img in All_images:

    if img is None:
        break
    fgmask = fgbg.apply(img)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Frame', img)
    cv2.imshow('FG MASK Frame', fgmask)

    cv2.waitKey(0)
    

cv2.destroyAllWindows()