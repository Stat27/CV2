import cv2

img = cv2.imread('./cv2open/lena.jpg', 1)
print(img)

cv2.imshow('image',img)
k = cv2.waitKey(0)

#if we press F, we close all windows
if k == 27:
    cv2.destroyAllWindows()
# if we press s, we save the image
elif k == ord('s'):
    cv2.imwrite('./cv2open/lena_copy.png',img)
    cv2.destroyAllWindows()