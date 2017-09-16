# Goal
# - Learn several arithmetic operation on images like addition, subtraction, bitwise operations etc.
# - You will learn these function : cv2.add(), cv2.addWeighted()

import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])

# difference between OpenCV addition and Numpy addition
print(cv2.add(x, y))    # 250 + 10 = 260 => 255
print(x + y)            # 250 + 10 = 260 % 256 = 4

# Image Blending
img1 = cv2.imread('C:/Users/Mig/Desktop/Ultraseven_rocket.jpg')
img2 = cv2.imread('C:/Users/Mig/Desktop/opencv-logo2.png')

img2_row, img2_col, temp = img2.shape
img1_cropp = img1[0:img2_row, 0:img2_col]



dst = cv2.addWeighted(img1_cropp, 0.7, img2, 0.3, 0)    # image must have same shape
#cv2.imshow('dst', dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# Bitwise Operations

row, col, channels = img2.shape
roi = img1[0:row, 0:col]


# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:row, 0:col] = dst

cv2.imshow('result', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
