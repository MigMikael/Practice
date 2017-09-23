import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
        cv2.rectangle(img1, (x-2, y-2), (x+2, y+2), (0, 255, 0), 1)
        cv2.rectangle(img2, (x-2, y-2), (x+2, y+2), (0, 255, 0), 1)
        print(x, y)


# Create a black image, a window and bind the function to window
img1 = cv2.imread('C:/Users/Mig/Desktop/seven.jpg')
img2 = cv2.imread('C:/Users/Mig/Desktop/seven.jpg')
#img = cv2.imread('C:/Users/Mig/Desktop/seven.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img1)
    cv2.imshow('image', img2)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()