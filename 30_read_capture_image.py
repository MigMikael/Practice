import cv2

sx, sy = 0, 0


def greetings():
    print("Welcome to auto region picker")


def read_image(path):
    img = cv2.imread(path)
    return img


def plot_coordinate(img, x, y, region, num):
    edit_img = img.copy()
    startX = x
    startY = y
    count = 0
    pixel_list = []

    for i in range(20):
        for j in range(16):
            bias_x = i // 5
            bias_y = j // 4

            '''
            # S8
            if num == 3 or num == 21 or num == 36 or num == 41 or num == 44 or num == 55 or num == 69:
                indexX, indexY = startX + 10 + (67 * i) - (bias_x * 8), startY + 10 + (67 * j) - (bias_y * 8)
            else:
                indexX, indexY = startX + 10 + (67 * i) - (bias_x * 5), startY + 10 + (67 * j) - (bias_y * 5)
            
            #motoC
            if num == 4 or num == 6 or num == 13:
                indexX, indexY = startX + 10 + (67 * i) - (bias_x * 8), startY + 10 + (67 * j) - (bias_y * 8)
            else:
                indexX, indexY = startX + 10 + (67 * i) - (bias_x * 5), startY + 10 + (67 * j) - (bias_y * 5)
            '''
            # iPad
            if num == 5 or num == 10 or num == 17 or num == 20 or num == 21 or num == 23 or num == 24 or num == 39 or num == 40 or num == 44 or num == 61 or num == 80 or num == 100:
                indexX, indexY = startX + 10 + (67 * i) - (bias_x * 8), startY + 10 + (67 * j) - (bias_y * 8)
            elif num == 74:
                indexX, indexY = startX + 10 + (67 * i) - (bias_x * 10), startY + 10 + (67 * j) - (bias_y * 10)
            else:
                indexX, indexY = startX + 10 + (67 * i) - (bias_x * 5), startY + 10 + (67 * j) - (bias_y * 5)


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
            pixel_list = collect_pixel_data2(sq1_crop, pixel_list)

            sq2_crop = img[index_sq2_y:index_sq1_y + region, index_sq2_x:index_sq2_x + region]
            sq2_crop = cv2.cvtColor(sq2_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq2_crop, pixel_list)

            sq3_crop = img[index_sq3_y:index_sq3_y + region, index_sq3_x:index_sq3_x + region]
            sq3_crop = cv2.cvtColor(sq3_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq3_crop, pixel_list)

            sq4_crop = img[index_sq4_y:index_sq4_y + region, index_sq4_x:index_sq4_x + region]
            sq4_crop = cv2.cvtColor(sq4_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq4_crop, pixel_list)

            sq5_crop = img[index_sq5_y:index_sq5_y + region, index_sq5_x:index_sq5_x + region]
            sq5_crop = cv2.cvtColor(sq5_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq5_crop, pixel_list)

            sq6_crop = img[index_sq6_y:index_sq6_y + region, index_sq6_x:index_sq6_x + region]
            sq6_crop = cv2.cvtColor(sq6_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq6_crop, pixel_list)

            sq7_crop = img[index_sq7_y:index_sq7_y + region, index_sq7_x:index_sq7_x + region]
            sq7_crop = cv2.cvtColor(sq7_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq7_crop, pixel_list)

            sq8_crop = img[index_sq8_y:index_sq8_y + region, index_sq8_x:index_sq8_x + region]
            sq8_crop = cv2.cvtColor(sq8_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq8_crop, pixel_list)

            sq9_crop = img[index_sq9_y:index_sq9_y + region, index_sq9_x:index_sq9_x + region]
            sq9_crop = cv2.cvtColor(sq9_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq9_crop, pixel_list)

            count += 1

    return pixel_list, edit_img


def collect_pixel_data(tiny_crop, pixel_list):
    for k in range(tiny_crop.shape[0]):
        for l in range(tiny_crop.shape[1]):
            r = tiny_crop[k][l][0]
            g = tiny_crop[k][l][1]
            b = tiny_crop[k][l][2]
            pixel_list.append([r, g, b])

    return pixel_list


def collect_pixel_data2(tiny_crop, pixel_list):
    for k in range(1, 6):       # 1 2 3 4 5
        for l in range(1, 6):   # 1 2 3 4 5
            center_x = k
            center_y = l
            sum_r, sum_g, sum_b = 0, 0, 0
            for m in range(center_x - 1, center_x + 2):
                for n in range(center_y - 1, center_y + 2):
                    sum_r += tiny_crop[m][n][0]
                    sum_g += tiny_crop[m][n][1]
                    sum_b += tiny_crop[m][n][2]

            r = int(round(sum_r / float(9)))
            g = int(round(sum_g / float(9)))
            b = int(round(sum_b / float(9)))
            pixel_list.append([r, g, b])

    return pixel_list


def collect_pixel_data3(tiny_crop, pixel_list):
    for k in range(2, 5):       # 2 3 4
        for l in range(2, 5):   # 2 3 4
            center_x = k
            center_y = l
            sum_r, sum_g, sum_b = 0, 0, 0
            for m in range(center_x - 2, center_x + 3):
                for n in range(center_y - 2, center_y + 3):
                    sum_r += tiny_crop[m][n][0]
                    sum_g += tiny_crop[m][n][1]
                    sum_b += tiny_crop[m][n][2]

            r = int(round(sum_r / float(25)))
            g = int(round(sum_g / float(25)))
            b = int(round(sum_b / float(25)))
            pixel_list.append([r, g, b])

    return pixel_list


def collect_pixel_data4(tiny_crop, pixel_list):
    r, g, b = 0, 0, 0
    for k in range(tiny_crop.shape[0]):
        for l in range(tiny_crop.shape[1]):
            r += tiny_crop[k][l][0]
            g += tiny_crop[k][l][1]
            b += tiny_crop[k][l][2]

    r = int(round(r / float(49)))
    g = int(round(g / float(49)))
    b = int(round(b / float(49)))
    pixel_list.append([r, g, b])

    return pixel_list


def write_file(file_name, the_list):
    with open(file_name, 'a') as outfile:
        for i in range(len(the_list)):
            data_line = str(the_list[i][0]) + " " + str(the_list[i][1]) + " " + str(the_list[i][2])
            data_line = data_line + "\n"
            outfile.write(data_line)
    #print("wrote file")


def write_image(write_path, image):
    cv2.imwrite(write_path, image)


region = 7
base_path = "C:\\Users\\Mig\\Documents\\Thesis\\"

ipad = "iPadMini4"
mi5 = "Mi5"
motoc = "MotoC"
gs8 = "S8+"

ipad_img_path = base_path + ipad + "\\data_set\\resize_img\\"
mi5_img_path = base_path + mi5 + "\\data_set\\resize_img\\"
motoc_img_path = base_path + motoc + "\\data_set\\resize_img\\"
gs8_img_path = base_path + gs8 + "\\data_set\\resize_img\\"

greetings()
write_file_name = ipad + "_data-14" + ".txt"

start_index_path = base_path + ipad + "\\data_set\\resize_img\\start_index.txt"

with open(start_index_path, 'r')as data_file:
    for line in data_file:
        no, x, y = line.split(",")

        img_name = "img"+no

        dev_img_path = ipad_img_path + img_name + ".jpg"
        device_img = read_image(dev_img_path)

        device_pixel_list, edit_image = plot_coordinate(device_img, int(x), int(y), region, int(no))

        write_image(ipad_img_path + img_name + "_plot.jpg", edit_image)

        write_file(ipad_img_path + write_file_name, device_pixel_list)

        print("Finish Image", no)
    print("Finish -------------")
