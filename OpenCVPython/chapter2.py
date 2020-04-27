import cv2
import numpy as np
# https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=443s
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)
imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imBlur = cv2.GaussianBlur(imGray,(7,7),0)
#in order to find the edges in an image
imgCanny = cv2.Canny(img, 200, 150)
#we are given two threshholds and we can choose where we go.
imgdial = cv2.dilate(imgCanny,kernel,iterations=1)
imgErode = cv2.erode(imgdial, kernel, iterations=1)

cv2.imshow("GrayImage",imGray)
cv2.imshow("BlurImages",imBlur)
cv2.imshow("CannyImage",imgCanny)
cv2.imshow("Image Dialation",imgdial)
cv2.imshow("Image Erode",imgErode)
cv2.waitKey(0)