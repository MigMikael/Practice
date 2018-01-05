import cv2
import os


iPad_image_path = "C:\\Users\\Mig\\Documents\\Thesis\\iPadMini4\\data_set\\"
s8_image_path = "C:\\Users\\Mig\\Documents\\Thesis\\S8+\\data_set\\"
motoC_image_path = "C:\\Users\\Mig\\Documents\\Thesis\\MotoC\\data_set\\"
Mi5_image_path = "C:\\Users\\Mig\\Documents\\Thesis\\Mi5\\data_set\\"

choose_img_path = s8_image_path

for filename in os.listdir(choose_img_path):
    original_image = cv2.imread(choose_img_path + filename)
    #newx, newy = (original_image.shape[1] * 1200) / 2448, (original_image.shape[0] * 1600) / 3264
    newx, newy = (original_image.shape[1] * 1200) / 3024, (original_image.shape[0] * 1600) / 4032
    #newx, newy = (original_image.shape[1] * 1200) / 1920, (original_image.shape[0] * 1600) / 2560
    #newx, newy = (original_image.shape[1] * 1200) / 3456, (original_image.shape[0] * 1600) / 4608
    new_image = cv2.resize(original_image, (int(newx), int(newy)))
    new_filename, extension = filename.split(".")
    cv2.imwrite(choose_img_path + "resize_img2\\" + new_filename + "_resize.jpg", new_image)
    print(filename, "Finish")
