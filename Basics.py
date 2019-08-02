import cv2
import pytest
import numpy as np


original = cv2.imread("Idris.jpg")
print(original.shape)
print(original.size)
print(original.dtype)
cv2.imshow("org", original)
print()

grayScale = cv2.imread("tiger.jpg",0)
print(grayScale.shape)
print(grayScale.size)
print(grayScale.dtype)
cv2.imshow("gary",grayScale)


cv2.waitKey(0)
