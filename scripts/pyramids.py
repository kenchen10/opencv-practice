import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('./data/sudoku.png')
lr = cv2.pyrDown(img)

cv2.imshow('image', img)
cv2.imshow('lr', lr)
cv2.waitKey(0)
cv2.destroyAllWindows()