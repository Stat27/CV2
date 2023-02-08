import cv2
import numpy as np

# read image
img = cv2.imread('./data/PIV_Camera_2020-02-12 12.52.28.657.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,mask = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

res_ = cv2.resize(img,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
mask = cv2.resize(mask,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
result = cv2.inpaint(res_, mask, 10, cv2.INPAINT_TELEA)
result = cv2.cvtColor(result,cv2.COLOR_GRAY2BGR)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.namedWindow("result", cv2.WINDOW_NORMAL)

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('result',result)

cv2.resizeWindow("img", 2448, 2080)
cv2.resizeWindow("mask", 2448, 2080)
cv2.resizeWindow("result", 2448, 2080)

cv2.waitKey(0)

cv2.imwrite('./Remove Glare/result.jpg',result)

