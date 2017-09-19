# Goal
# - measure performance of code
# - tips to improve performance of code
# - use function cv2.getTickCount, cv2.getTickFrequency

import cv2

img1 = cv2.imread('C:/Users/Mig/Desktop/Ultraseven_rocket.jpg')

e1 = cv2.getTickCount()

# do something here
for i in range(5, 50, 2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()
time = (e2 - e1) / cv2.getTickFrequency()
print(time)

# check if optimization is enabled
print(cv2.useOptimized())

res = cv2.medianBlur(img1, 49)
print(res)