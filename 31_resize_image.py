import cv2

'''
motoC_filename = "C:\\Users\\Mig\\PycharmProjects\\Practice\\capture_image\\IMG_20171231_162833"
original_image = cv2.imread(motoC_filename + ".jpg")
newx, newy = (original_image.shape[1]*1200)/1920, (original_image.shape[0]*1600)/2560
new_image = cv2.resize(original_image, (int(newx), int(newy)))
cv2.imwrite(motoC_filename+"_resize.jpg", new_image)
print("Finish")
'''

Mi5_filename = ""
iPad_filename = ""

galaxy_s8_filename = "C:\\Users\\Mig\\PycharmProjects\\Practice\\capture_image\\20171231_182926"
original_image = cv2.imread(galaxy_s8_filename + ".jpg")
newx, newy = (original_image.shape[1]*1200)/3024, (original_image.shape[0]*1600)/4032
new_image = cv2.resize(original_image, (int(newx), int(newy)))
cv2.imwrite(galaxy_s8_filename+"_resize.jpg", new_image)
print("Finish")

