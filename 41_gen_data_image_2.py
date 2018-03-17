import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

color_list = []
for i in range(256):
    for j in range(256):
        for k in range(256):
            if i % 8 == 0 and j % 8 == 0 and k % 8 == 0:
                color_list.append([i, j, k])
print(len(color_list))

for k in range((len(color_list) // 1026)+1):
    img_name = "the_image_"+str(k+1)+".png"
    save_path = "C:\\Users\\Mig\\PycharmProjects\\Practice\\gen_image_4\\"
    height, width = 2480, 3508  # A4 paper 300 PPI
    the_image = np.zeros((height, width, 3), np.uint8)
    the_image[:, 0:width] = (255, 255, 255)  # (B, G, R)

    cv2.rectangle(the_image, (5, 5), (3503, 2475), (0, 0, 0), 5)

    count = 0
    for i in range(38):
        for j in range(27):
            # print((320*k) + count)
            index = (1026 * k) + count
            if index >= len(color_list):
                R, G, B = 255, 255, 255
            else:
                R = color_list[index][0]
                G = color_list[index][1]
                B = color_list[index][2]
                # print(R, G, B)

            cv2.rectangle(the_image, (30 + (90 * i), 30 + (90 * j)), (110 + (90 * i), 110 + (90 * j)), (B, G, R),
                          -1)
            count += 1
    cv2.putText(the_image, str(k + 1), (3443, 70), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imwrite(save_path + img_name, the_image)
    print("Finish write " + img_name)
    #break

print("Finish")
