import cv2
import numpy as np


img = cv2.imread("Idris.jpg")




smooth = cv2.GaussianBlur(img,(9,9),0)

unsharp = cv2.addWeighted(img,0.9,smooth,0.3,0)


cv2.imshow("Original",img)
cv2.imshow("Smooth",smooth)
cv2.imshow("unsharp",unsharp)


cv2.waitKey(0)