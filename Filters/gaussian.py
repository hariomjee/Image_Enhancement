import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('noise.jpg')
blur = cv.GaussianBlur(img,(5,5),0)

plt.subplot(),plt.imshow(blur),plt.title('Gaussian filter')
plt.xticks([]), plt.yticks([])
plt.show()