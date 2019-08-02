import cv2
import numpy as np

orig = cv2.imread("tiger.jpg",)

kernal_3 = (11,11)


cv2.imshow("orignal", orig)

dilate = cv2.dilate(orig,kernal_3,iterations=1)

erode = cv2.erode(orig,kernal_3,iterations=1)
cv2.imshow("dilated", dilate)
cv2.imshow("erode",erode)

opening = cv2.morphologyEx(orig, cv2.MORPH_OPEN,kernel=kernal_3)

openingOrig = np.concatenate((opening,orig,),axis= 1 )

cv2.imshow("opening", openingOrig)
cv2.waitKey(0)