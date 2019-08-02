import cv2
import numpy as np

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255),
          'black': (0, 0, 0), 'gray': (125, 125, 125),
          'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

image = np.zeros((500,500,3), dtype= "uint8")

image[:] = colors['light_gray']

sepration = 40


cv2.line(image, (100, 400), (50, 0), colors['yellow'], 8, lineType=cv2.LINE_8, shift=0)
cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['red'], 2, cv2.LINE_4)
cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['red'], 2, cv2.LINE_8)
cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['red'], 2, cv2.LINE_AA)
cv2.imshow('line8', image)

cv2.waitKey(0)

  