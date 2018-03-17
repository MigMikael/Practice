import numpy as np
import cv2


def order_points(pts):
    rect = np.zeros((4,2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped


image_path = "C:\\Users\\Mig\\PycharmProjects\\Practice\\capture_image\\img_test.jpg"
image = cv2.imread(image_path)
with open('C:\\Users\\Mig\\PycharmProjects\\Practice\\capture_image\\coord4.txt', 'r') as coord_file:
    line = coord_file.read()
    point1, point2, point3, point4 = line.split('|')
    point1_x, point1_y = point1.split(',')
    point2_x, point2_y = point2.split(',')
    point3_x, point3_y = point3.split(',')
    point4_x, point4_y = point4.split(',')
    rec = np.array([
        [int(point1_x), int(point1_y)],
        [int(point2_x), int(point2_y)],
        [int(point3_x), int(point3_y)],
        [int(point4_x), int(point4_y)]
    ])
    print(rec)
    warped = four_point_transform(image, rec)

    cv2.imshow("original", image)
    cv2.imshow("warped", warped)
    cv2.waitKey(0)