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
#print(color_list)

for k in range((len(color_list) // 320)+1):
    img_name = "the_image_"+str(k+1)+".png"
    save_path = "C:\\Users\\Mig\\PycharmProjects\\Practice\\gen_image_2\\"
    height, width = 2480, 3508  # A4 paper 300 PPI

    the_image = np.zeros((height, width, 3), np.uint8)
    the_image[:, 0:width] = (255, 255, 255)  # (B, G, R)
    count = 0
    for i in range(20):
        for j in range(16):
            #print((320*k) + count)
            index = (320*k) + count
            if index >= len(color_list):
                R, G, B = 255, 255, 255
            else:
                R = color_list[index][0]
                G = color_list[index][1]
                B = color_list[index][2]
                #print(R, G, B)

            cv2.rectangle(the_image,  (200+(120*i), 200+(120*j)), (310+(120*i), 310+(120*j)), (B, G, R), -1)
            count += 1
    cv2.putText(the_image, str(k+1), (2600, 400), font, 6, (0, 0, 0), 15, cv2.LINE_AA)
    cv2.rectangle(the_image, (100, 100), (3000, 2246), (0, 0, 0), 25)
    cv2.imwrite(save_path+img_name, the_image)
    #print("write---------------")

print("Finish")


