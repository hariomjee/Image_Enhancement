import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('noise.jpg')
median = cv.medianBlur(img,5)

plt.subplot(),plt.imshow(median),plt.title('Median filter')
plt.xticks([]), plt.yticks([])
plt.show()