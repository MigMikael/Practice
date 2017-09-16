# Goal
# - Access pixel value and modify them
# - Access image properties
# - Setting Region of Image(ROI)
# - Splitting and Merging images

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Accessing and Modifying pixel value
img = cv2.imread('C:/Users/Mig/Desktop/emerium_1.jpg')

# Access pixel
px = img[100, 50]
print(px)   # [255 155  96]

# Access only blue value in pixel
blue = img[100, 50, 0]
print(blue)

green = img[100, 50, 1]
print(green)

red = img[100, 50, 2]
print(red)
print()


# Better pixel accessing and editing
print(img.item(100, 50, 2))

img.itemset((100, 50, 2), 200)
print(img.item(100, 50, 2))
print()

# How about access pixel not in image
print(img.item(300, 400, 0))
print()
print()


# Accessing Image Properties
print(img.shape)    # dimension
print(img.size)     # total pixel = 451584
print(img.dtype)    # data type


# Image ROI
something = img[250:300, 300:350]
img[100:150, 150:200] = something
#cv2.imwrite('C:/Users/Mig/Desktop/emerium_1_editt.jpg', img)
print("finish")
print()


# Splitting and Merging Image Channels
b, g, r = cv2.split(img)
print(b.shape)
print(b.dtype)
print(b.size)       # 1/3 of image size = 150528
print()

# or get blue like this
bb = img[:, :, 0]
print(bb.shape)
print(bb.dtype)
print(bb.size)

# set all red pixel to zero
img[:, :, 2] = 0
#cv2.imshow('remove-rad-image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# Making Borders for Images (Padding)
BLUE = [255, 0, 0]

img1 = cv2.imread('C:/Users/Mig/Desktop/opencv-logo2.png')

replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231)
plt.imshow(img1, 'gray')
plt.title('original')

plt.subplot(232)
plt.imshow(replicate, 'gray')
plt.title('replicate')

plt.subplot(233)
plt.imshow(reflect, 'gray')
plt.title('reflect')

plt.subplot(234)
plt.imshow(reflect_101, 'gray')
plt.title('reflect_101')

plt.subplot(235)
plt.imshow(wrap, 'gray')
plt.title('wrap')

plt.subplot(236)
plt.imshow(constant, 'gray')
plt.title('constant')

plt.show()
# Image is displayed with matplotlib. So RED and BLUE planes will be interchanged





