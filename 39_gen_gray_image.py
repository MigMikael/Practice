import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

color_list = [c for c in range(256)]


img_name = "the_image_" + str(104) + ".png"
save_path = "C:\\Users\\Mig\\PycharmProjects\\Practice\\gen_image_3\\"
height, width = 2480, 3508  # A4 paper 300 PPI

the_image = np.zeros((height, width, 1), np.uint8)
the_image[:, 0:width] = 255  # (B, G, R)

count = 0
for i in range(20):
    for j in range(16):
        if count > 255:
            count = 255
        cv2.rectangle(the_image,  (200+(120*i), 200+(120*j)), (310+(120*i), 310+(120*j)), (color_list[count]), -1)
        count += 1

cv2.putText(the_image, str(104), (2600, 400), font, 6, (0, 0, 0), 15, cv2.LINE_AA)
cv2.rectangle(the_image, (100, 100), (3000, 2246), (0, 0, 0), 25)
cv2.imwrite(save_path+img_name, the_image)