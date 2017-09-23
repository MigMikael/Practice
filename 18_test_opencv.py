import cv2
import numpy as np

img = cv2.imread('C:/Users/Mig/Desktop/Microsoft-Logo-3.jpg')
#cv2.imshow('image', img)
#cv2.waitKey(0)
print(img.shape)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite('C:/Users/Mig/Desktop/UM-002_gray.jpg', gray)

tiny_crop = img[262:238, 266:242]
print(tiny_crop.shape)

'''
cv2.imshow('tiny-crop', tiny_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#print(img[437, 365])

