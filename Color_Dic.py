import cv2
import numpy as np

#Dictionary containing some colors

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255),
          'black': (0, 0, 0), 'gray': (125, 125, 125),
          'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

#making a canvas for drawing the lines

image = np.zeros((500, 500, 3), dtype= "uint8")


image[:] = colors['dark_gray']

seperation = 40

for key in colors:
    cv2.line(image,(0,seperation),(500,seperation),colors[key],10)
    seperation += 40

cv2.imshow("lines",image)

cv2.waitKey(0)