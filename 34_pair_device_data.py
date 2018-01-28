import time

label_data = "C:\\Users\\Mig\\Documents\\Thesis\\S8+\\data_set\\resize_img\\S8+_data.txt"
feature_data = "C:\\Users\\Mig\\Documents\\Thesis\\MotoC\\data_set\\resize_img\\MotoC_data.txt"
output_data = "C:\\Users\\Mig\\Documents\\Thesis\\s8_motoC\\s8_motoC_data_8.txt"

start_time = time.time()

label_file = open(label_data, "r")
feature_file = open(feature_data, "r")

label_RGB_list = label_file.readlines()
feature_RGB_list = feature_file.readlines()

length = len(label_RGB_list)
print("Label : ", length)

length2 = len(feature_RGB_list)
print("Feature : ", length2)

with open(output_data, "w") as outfile:
    jump_index = 0
    for i in range(length):
        if i % 7 == 0:
            jump_index = i

        label_temp = label_RGB_list[jump_index].replace("\n", "")
        feature_temp = feature_RGB_list[i].replace("\n", "")

        line = "|labels " + label_temp + " |features " + feature_temp + "\n"
        outfile.write(line)
        if i < 14:
            print(line)

label_file.close()
feature_file.close()

print("--- %s ---" % (time.time() - start_time))
print("Finish")