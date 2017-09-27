import cv2
import numpy as np

# mouse callback function
def draw_rectangle1(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img1, (x-2, y-2), (x+2, y+2), (0, 255, 0), 1)
        print(x, y)

# mouse callback function
def draw_rectangle2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img2, (x - 2, y - 2), (x + 2, y + 2), (0, 255, 0), 1)
        print(x, y)


# Create a black image, a window and bind the function to window
img1 = cv2.imread('C:/Users/Mig/Desktop/seven.jpg')
img2 = cv2.imread('C:/Users/Mig/Desktop/seven.jpg')

cv2.namedWindow('image1')
cv2.setMouseCallback('image1', draw_rectangle1)

cv2.namedWindow('image2')
cv2.setMouseCallback('image2', draw_rectangle2)

while(1):
    cv2.imshow('image1', img1)
    cv2.imshow('image2', img2)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()