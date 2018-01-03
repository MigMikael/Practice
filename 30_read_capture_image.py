import cv2

sx, sy = 0, 0


def greetings():
    print("Welcome to auto region picker")
    print("------------------")
    print("Choose Pair Device")
    print("------------------")
    print("(1) iPad Mini 4")
    print("(2) Mi 5")
    print("(3) Moto C")
    print("(4) Galaxy S8+")
    print("------------------")
    dev1_no = int(input("Device 1 No : "))
    dev2_no = int(input("Device 2 No : "))
    return dev1_no, dev2_no


def read_image(path):
    img = cv2.imread(path)
    return img


def plot_coordinate(img, region):
    edit_img = img.copy()
    startX = int(input("Input start X Coordinate : "))
    startY = int(input("Input start Y Coordinate : "))
    count = 0
    pixel_list = []
    for i in range(20):
        for j in range(16):
            indexX, indexY = startX + 10 + (66 * i), startY + 10 + (66 * j)

            index_sq1_x, index_sq1_y = indexX, indexY
            index_sq2_x, index_sq2_y = indexX + 9, indexY
            index_sq3_x, index_sq3_y = indexX + 18, indexY

            index_sq4_x, index_sq4_y = indexX, indexY + 9
            index_sq5_x, index_sq5_y = indexX + 9, indexY + 9
            index_sq6_x, index_sq6_y = indexX + 18, indexY + 9

            index_sq7_x, index_sq7_y = indexX, indexY + 18
            index_sq8_x, index_sq8_y = indexX + 9, indexY + 18
            index_sq9_x, index_sq9_y = indexX + 18, indexY + 18

            cv2.rectangle(edit_img, (index_sq1_x, index_sq1_y), (index_sq1_x + region, index_sq1_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq2_x, index_sq2_y), (index_sq2_x + region, index_sq2_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq3_x, index_sq3_y), (index_sq3_x + region, index_sq3_y + region),
                          (255, 255, 255), 1)

            cv2.rectangle(edit_img, (index_sq4_x, index_sq4_y), (index_sq4_x + region, index_sq4_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq5_x, index_sq5_y), (index_sq5_x + region, index_sq5_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq6_x, index_sq6_y), (index_sq6_x + region, index_sq6_y + region),
                          (255, 255, 255), 1)

            cv2.rectangle(edit_img, (index_sq7_x, index_sq7_y), (index_sq7_x + region, index_sq7_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq8_x, index_sq8_y), (index_sq8_x + region, index_sq8_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq9_x, index_sq9_y), (index_sq9_x + region, index_sq9_y + region),
                          (255, 255, 255), 1)

            sq1_crop = img[index_sq1_y:index_sq1_y + region, index_sq1_x:index_sq1_x + region]
            sq1_crop = cv2.cvtColor(sq1_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data(sq1_crop, pixel_list)

            sq2_crop = img[index_sq2_y:index_sq1_y + region, index_sq2_x:index_sq2_x + region]
            sq2_crop = cv2.cvtColor(sq2_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data(sq2_crop, pixel_list)

            sq3_crop = img[index_sq3_y:index_sq3_y + region, index_sq3_x:index_sq3_x + region]
            sq3_crop = cv2.cvtColor(sq3_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data(sq3_crop, pixel_list)

            sq4_crop = img[index_sq4_y:index_sq4_y + region, index_sq4_x:index_sq4_x + region]
            sq4_crop = cv2.cvtColor(sq4_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data(sq4_crop, pixel_list)

            sq5_crop = img[index_sq5_y:index_sq5_y + region, index_sq5_x:index_sq5_x + region]
            sq5_crop = cv2.cvtColor(sq5_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data(sq5_crop, pixel_list)

            sq6_crop = img[index_sq6_y:index_sq6_y + region, index_sq6_x:index_sq6_x + region]
            sq6_crop = cv2.cvtColor(sq6_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data(sq6_crop, pixel_list)

            sq7_crop = img[index_sq7_y:index_sq7_y + region, index_sq7_x:index_sq7_x + region]
            sq7_crop = cv2.cvtColor(sq7_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data(sq7_crop, pixel_list)

            sq8_crop = img[index_sq8_y:index_sq8_y + region, index_sq8_x:index_sq8_x + region]
            sq8_crop = cv2.cvtColor(sq8_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data(sq8_crop, pixel_list)

            sq9_crop = img[index_sq9_y:index_sq9_y + region, index_sq9_x:index_sq9_x + region]
            sq9_crop = cv2.cvtColor(sq9_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data(sq9_crop, pixel_list)

            count += 1

    cv2.imshow("read_image", edit_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return pixel_list


def collect_pixel_data(tiny_crop, pixel_list):
    for k in range(tiny_crop.shape[0]):
        for l in range(tiny_crop.shape[1]):
            r = tiny_crop[k][l][0]
            g = tiny_crop[k][l][1]
            b = tiny_crop[k][l][2]
            pixel_list.append([r, g, b])

    return pixel_list


def write_file(list_one, list_two, file_name):
    with open(file_name, 'w') as outfile:
        for i in range(len(list_one)):
            data_line = "|labels " + str(list_one[i][0]) + " " + str(list_one[i][1]) + " " + str(list_one[i][2])
            data_line = data_line + " |features " + str(list_two[i][0]) + " " + str(list_two[i][1]) + " " + str(list_two[i][2])
            data_line = data_line + "\n"
            outfile.write(data_line)
    print("wrote file")


region = 7
base_path = "C:\\Users\\Mig\\Documents\\Thesis\\"
ipad = "iPadMini4"
mi5 = "Mi5"
motoc = "MotoC"
gs8 = "S8+"

ipad_img_path = base_path + ipad + "\\data_set\\"
mi5_img_path = base_path + mi5 + "\\data_set\\"
motoc_img_path = base_path + motoc + "\\data_set\\"
gs8_img_path = base_path + gs8 + "\\data_set\\"


device1_no, device2_no = greetings()

choose_device_1, choose_device_2 = "", ""
dev1_img_path, dev2_img_path = "", ""

if device1_no == 1:
    choose_device_1 = ipad
    dev1_img_path = ipad_img_path
elif device1_no == 2:
    choose_device_1 = mi5
    dev1_img_path = mi5_img_path
elif device1_no == 3:
    choose_device_1 = motoc
    dev1_img_path = motoc_img_path
elif device1_no == 4:
    choose_device_1 = gs8
    dev1_img_path = gs8_img_path

if device2_no == 1:
    choose_device_2 = ipad
    dev2_img_path = ipad_img_path
elif device2_no == 2:
    choose_device_2 = mi5
    dev2_img_path = mi5_img_path
elif device2_no == 3:
    choose_device_2 = motoc
    dev2_img_path = motoc_img_path
elif device2_no == 4:
    choose_device_2 = gs8
    dev2_img_path = gs8_img_path

write_data_path = base_path + choose_device_1 + "_" + choose_device_2 + "\\"

for i in range(103):
    write_file_name = choose_device_1+"_"+choose_device_2+"_"+str(i+1)+".txt"
    dev1_img_path = dev1_img_path + "img"+str(i+1)+".jpg"
    dev2_img_path = dev2_img_path + "img"+str(i+1)+".jpg"

    device1_img = read_image(dev1_img_path)
    device2_img = read_image(dev2_img_path)

    device1_pixel_list = plot_coordinate(device1_img, region)
    device2_pixel_list = plot_coordinate(device2_img, region)

    write_file(device1_pixel_list, device2_pixel_list, write_data_path + write_file_name)
    print("Finish Image", i+1)
