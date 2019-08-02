import  cv2
import numpy as np


image =cv2.imread("Idris.jpg")

height , width = image.shape[:2]
dst_image = cv2.resize(image, (width*2,height*2), interpolation=cv2.INTER_CUBIC)


M = np.float32([[1, 0, -50],[0,1,-30]])

translate = cv2.warpAffine(image,M, (width,height))

M = cv2.getRotationMatrix2D((width/2.0,height/2.0),180,1)

Rotate = cv2.warpAffine(image,M,(width,height))
#
# cv2.imshow("Resized", dst_image)
# cv2.imshow("Original", image)
# cv2.imshow("Resized", dst_image)
cv2.imshow("Rotate", Rotate)
cv2.waitKey(0)



