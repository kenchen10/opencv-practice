import cv2

path = 'data/'
img = cv2.imread(path + 'lena.jpg', 0)
print(img)
