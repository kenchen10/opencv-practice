import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('./data/sudoku.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
g_blur = cv2.GaussianBlur(img, (5, 5), 0)

titles = ['image', '2D Conv', 'blur', 'Gaussian']
images = [img, dst, blur, g_blur]

for i in range(len(images)):
    plt.subplot(1, len(images), i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()