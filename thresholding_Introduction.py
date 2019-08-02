import cv2
import numpy as np
from matplotlib import pyplot as plt


def show_with_matplotlib(image,title,pos):

    img_rgb = image[:,:,::-1]

    ax = plt.subplot(8,1,pos)

    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis("off")

def buid_sample_image():

    tones = np.arange(start = 50,stop=300,step = 50)

    result = np.zeros((50,50,3), dtype = "uint8")

    for tone in tones:
        img = np.ones((50,50,3), dtype= 'uint8') * tone
        result = np.concatenate((result,img), axis= 1)

    return result



fig = plt.figure(figsize=(10,14))
plt.suptitle("thresolding functiom", fontsize = 14)
fig.patch.set_facecolor('silver')


image = buid_sample_image()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret1, thresh1 = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)
ret3, thresh3 = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
ret4, thresh4 = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
ret5, thresh5 = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
ret6, thresh6 = cv2.threshold(gray_image, 250, 255, cv2.THRESH_BINARY)


# show_with_matplotlib(cv2.cvtColor(thresh1, cv2.COLOR_GRAY2BGR), "threshold = 0", 2))
# show_with_matplotlib(cv2.cvtColor(thresh2, cv2.COLOR_GRAY2BGR), "threshold = 50", 3))
# show_with_matplotlib(cv2.cvtColor(thresh3, cv2.COLOR_GRAY2BGR), "threshold = 100", 4))
# show_with_matplotlib(cv2.cvtColor(thresh4, cv2.COLOR_GRAY2BGR), "threshold = 150", 5))
# show_with_matplotlib(cv2.cvtColor(thresh5, cv2.COLOR_GRAY2BGR), "threshold = 200", 6))
# show_with_matplotlib(cv2.cvtColor(thresh6, cv2.COLOR_GRAY2BGR), "threshold = 250", 7))
show_with_matplotlib(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR),
                         "img with tones of gray - left to right: (0,50,100,150,200,250)", 1)

show_with_matplotlib(cv2.cvtColor(thresh1, cv2.COLOR_GRAY2BGR), "threshold = 0", 2)


show_with_matplotlib(cv2.cvtColor(thresh1, cv2.COLOR_GRAY2BGR), "threshold = 0", 3)
show_with_matplotlib(cv2.cvtColor(thresh2, cv2.COLOR_GRAY2BGR), "threshold = 50", 4)
show_with_matplotlib(cv2.cvtColor(thresh3, cv2.COLOR_GRAY2BGR), "threshold = 100", 5)
show_with_matplotlib(cv2.cvtColor(thresh4, cv2.COLOR_GRAY2BGR), "threshold = 150", 6)
show_with_matplotlib(cv2.cvtColor(thresh5, cv2.COLOR_GRAY2BGR), "threshold = 200", 7)
show_with_matplotlib(cv2.cvtColor(thresh6, cv2.COLOR_GRAY2BGR), "threshold = 250", 8)

plt.show()







