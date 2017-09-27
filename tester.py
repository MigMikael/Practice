import cv2

path = 'C:/Users/Mig/Desktop/test_image/img1.jpg'


img = cv2.imread(path)
print(img[774, 1948])
print(img[1020, 2295])
print(img[1125, 2233])


path = 'C:/Users/Mig/Desktop/test_image/img2.jpg'
path2 = 'C:/Users/Mig/Desktop/emerium_1.jpg'

img = cv2.imread(path)

tiny_crop = img[3096:3096 + 100, 1246:1246 + 100]
print(tiny_crop[0][0])
print(tiny_crop.shape)
cv2.imshow('tiny-crop', tiny_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
