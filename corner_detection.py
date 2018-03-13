import numpy
import cv2

image = cv2.imread('C:\\Users\\Mig\\PycharmProjects\\Practice\\capture_image\\img6.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = numpy.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 1)
corners = numpy.int0(corners)
#print(corners)


for corner in corners:
    #print(corner[0][0])
    x, y = corner[0][0], corner[0][1]
    cv2.circle(image, (x, y), 3, 255, -1)

cv2.imshow('Corner', image)
cv2.waitKey(0)