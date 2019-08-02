# Import required packages:
import cv2
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
from skimage import img_as_ubyte


def show_img_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(2, 2, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


def show_hist_with_matplotlib_gray(hist, title, pos, color, t=-1):
    """Shows the histogram using matplotlib capabilities"""

    ax = plt.subplot(2, 2, pos)
    # plt.title(title)
    plt.xlabel("bins")
    plt.ylabel("number of pixels")
    plt.xlim([0, 256])
    plt.axvline(x=t, color='m', linestyle='--')
    plt.plot(hist, color=color)


# Create the dimensions of the figure and set title and color:
fig = plt.figure(figsize=(8, 8))
plt.suptitle("Thresholding scikit-image (Otsu's binarization example)", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

# Load the image and convert it to grayscale:
image = cv2.imread('leaf.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray_image], [0], None ,[256],[0,255])
#----------------------------------------------Scikit-----Code----------------------------
thres = threshold_otsu(gray_image)
binary = gray_image < thres

binary  = img_as_ubyte(binary)


show_img_with_matplotlib(image, "image", 1)
show_img_with_matplotlib(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR), "gray img", 2)
show_hist_with_matplotlib_gray(hist, "grayscale histogram", 3, 'm', thres)
show_img_with_matplotlib(cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR), "Otsu's binarization (scikit-image)", 4)


plt.show()