import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
#print(img)
#img[200:300,100:200] = 255,0,0 #this entire picture will be blue

cv2.line(img,(0,0),(300,300),(0,355,0),3)
#cv2.line -->image, area, sp, ep, thickness of line
cv2.imshow("Image",img)
cv2.waitKey(0)