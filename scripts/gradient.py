import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('./data/sudoku.png', cv2.IMREAD_GRAYSCALE)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.abs(lap))
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel_x = np.uint8(np.abs(sobel_x))
sobel_y = np.uint8(np.abs(sobel_y))
sobel = cv2.bitwise_or(sobel_x, sobel_y)

titles = ['image', 'lap', 'sob_x', 'sob_y', 'sob']
images = [img, lap, sobel_x, sobel_y, sobel]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()