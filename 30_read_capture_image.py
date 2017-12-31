import cv2

cap_img = cv2.imread('C:\\Users\\Mig\\PycharmProjects\\Practice\\capture_image\\20171231_182926_resize.jpg')
#cap_img = cv2.imread('C:\\Users\\Mig\\PycharmProjects\\Practice\\capture_image\\IMG_20171231_162833_resize.jpg')

startX, startY = 15, 65
#startX, startY = 22, 47
region = 7

count = 0
for i in range(20):
    for j in range(15):
        indexX, indexY = startX+10+(67*i), startY+10+(67*j)

        index_sq1_x, index_sq1_y = indexX, indexY
        index_sq2_x, index_sq2_y = indexX + 9, indexY
        index_sq3_x, index_sq3_y = indexX + 18, indexY

        index_sq4_x, index_sq4_y = indexX, indexY + 9
        index_sq5_x, index_sq5_y = indexX + 9, indexY + 9
        index_sq6_x, index_sq6_y = indexX + 18, indexY + 9

        index_sq7_x, index_sq7_y = indexX, indexY + 18
        index_sq8_x, index_sq8_y = indexX + 9, indexY + 18
        index_sq9_x, index_sq9_y = indexX + 18, indexY + 18

        cv2.rectangle(cap_img, (index_sq1_x, index_sq1_y), (index_sq1_x + region, index_sq1_y + region), (255, 255, 255), 1)
        cv2.rectangle(cap_img, (index_sq2_x, index_sq2_y), (index_sq2_x + region, index_sq2_y + region), (255, 255, 255), 1)
        cv2.rectangle(cap_img, (index_sq3_x, index_sq3_y), (index_sq3_x + region, index_sq3_y + region), (255, 255, 255), 1)

        cv2.rectangle(cap_img, (index_sq4_x, index_sq4_y), (index_sq4_x + region, index_sq4_y + region), (255, 255, 255), 1)
        cv2.rectangle(cap_img, (index_sq5_x, index_sq5_y), (index_sq5_x + region, index_sq5_y + region), (255, 255, 255), 1)
        cv2.rectangle(cap_img, (index_sq6_x, index_sq6_y), (index_sq6_x + region, index_sq6_y + region), (255, 255, 255), 1)

        cv2.rectangle(cap_img, (index_sq7_x, index_sq7_y), (index_sq7_x + region, index_sq7_y + region), (255, 255, 255), 1)
        cv2.rectangle(cap_img, (index_sq8_x, index_sq8_y), (index_sq8_x + region, index_sq8_y + region), (255, 255, 255), 1)
        cv2.rectangle(cap_img, (index_sq9_x, index_sq9_y), (index_sq9_x + region, index_sq9_y + region), (255, 255, 255), 1)

        if count == 0:
            sq1_crop = cap_img[index_sq1_x:index_sq1_x + region, index_sq1_y:index_sq1_y + region]
            sq1_crop = cv2.cvtColor(sq1_crop, cv2.COLOR_BGR2RGB)
            print(sq1_crop)
        count += 1

cv2.imshow("read_image", cap_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
