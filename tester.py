import cv2

path = 'C:/Users/Mig/Desktop/test_image/img1.jpg'


img = cv2.imread(path)
print(img[774, 1948])
print(img[1020, 2295])
print(img[1125, 2233])


path = 'C:/Users/Mig/Desktop/test_image/img2.jpg'

img = cv2.imread(path)
print(img[1359, 2386])
print(img[1578, 2854])
print(img[1741, 2783])
