import os
import cv2

img_path = "C:\\Users\\Mig\\Documents\\Thesis\\iPadMini4\\additional_img\\resize_img\\"
count = 2
for filename in os.listdir(img_path):
    original_image = cv2.imread(img_path + filename)
    cv2.imwrite(img_path + "img" + str(count) + ".jpg", original_image)
    count += 1
    print("Finish", filename)

