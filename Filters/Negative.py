import cv2
img=cv2.imread('nature.jpg')
img1=255-img
cv2.imshow('negative',img1)
cv2.waitKey(0)