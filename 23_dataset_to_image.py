import cv2
import numpy as np

with open('C:/Users/Mig/Desktop/data-text.txt', 'r') as readfile:
    content = readfile.read()

print(type(content))

content_arr = np.fromstring(content)
print(type(content_arr))

'''
img = cv2.imread('C:/Users/Mig/Desktop/seven.jpg')
print(type(img))
print(type(img[10, 10]))
'''