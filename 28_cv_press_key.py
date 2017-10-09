import cv2

img1 = cv2.imread('C:/Users/Mig/Desktop/seven.jpg')
while(True):
    cv2.imshow('image1', img1)
    c = cv2.waitKey(0)
    print(c)
    if 'q' == chr(c & 255):
        print("You press Q ")