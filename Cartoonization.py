import cv2
import numpy as np



img = cv2.imread("tiger.jpg")


def sketch_image(img):
    """Sketches the image applying a laplacian operator to detect the edges"""

    # Convert to gray scale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median filter
    img_gray = cv2.medianBlur(img_gray, 5)

    # Detect edges using cv2.Laplacian()
    # edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)

    edges = cv2.Canny(img_gray,25,100)

    # Threshold the edges image:
    ret, thresholded = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)

    return thresholded


def cartonize_image(img, gray_mode=False):
    """Cartoonizes the image applying cv2.bilateralFilter()"""

    # Get the sketch:
    thresholded = sketch_image(img)

    # Apply bilateral filter with "big numbers" to get the cartoonized effect:
    filtered = cv2.bilateralFilter(img, 10, 250, 250)

    # Perform 'bitwise and' with the thresholded img as mask in order to set these values to the output
    cartoonized = cv2.bitwise_and(filtered, filtered, mask=thresholded)

    if gray_mode:
        return cv2.cvtColor(cartoonized, cv2.COLOR_BGR2GRAY)

    return cartoonized





# Call the created functions for sketching and cartoonizing images:
custom_sketch_image = sketch_image(img)
custom_cartonized_image = cartonize_image(img)
custom_cartonized_image_gray = cartonize_image(img, True)


cv2.imshow("Custom_Sketch", custom_sketch_image)
cv2.imshow("Custom Cartoonized", custom_cartonized_image)
cv2.imshow("custom_cartoonized_gary", custom_cartonized_image_gray)
cv2.imshow("original", img)
#
# dst = cv2.stylization(img, sigma_s=10, sigma_r=0.02)
# dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
#
# cv2.imshow("original",img)
# cv2.imshow("stylizated", dst)
#
# cv2.imshow("pencil gray", dst_gray)
#
# cv2.imshow("pencil ", dst_color)

cv2.waitKey(0)