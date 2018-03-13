import cv2

sx, sy = 0, 0


def greetings():
    print("Welcome to skin auto region picker")


def read_image(path):
    img = cv2.imread(path)
    return img


def plot_coordinate(img, edit_img, indexX, indexY, region):
    pixel_list = []

    index_sq1_x, index_sq1_y = indexX, indexY
    index_sq2_x, index_sq2_y = indexX + 14, indexY
    index_sq3_x, index_sq3_y = indexX + 28, indexY

    index_sq4_x, index_sq4_y = indexX, indexY + 14
    index_sq5_x, index_sq5_y = indexX + 14, indexY + 14
    index_sq6_x, index_sq6_y = indexX + 28, indexY + 14

    index_sq7_x, index_sq7_y = indexX, indexY + 28
    index_sq8_x, index_sq8_y = indexX + 14, indexY + 28
    index_sq9_x, index_sq9_y = indexX + 28, indexY + 28

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

    print(len(pixel_list))
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
    for k in range(1, 6):  # 1 2 3 4 5
        for l in range(1, 6):  # 1 2 3 4 5
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
    # print("wrote file")


def write_image(write_path, image):
    cv2.imwrite(write_path, image)


region = 7
source_image = "C:\\Users\\Mig\\Documents\\Thesis\\S8+\\Arm(S8+)_resize.jpg"
plot_image = "C:\\Users\\Mig\\Documents\\Thesis\\S8+\\Arm(S8+)_resize_plot.jpg"
start_index_path = "C:\\Users\\Mig\\Documents\\Thesis\\S8+\\start_index.txt"
write_file_name = "C:\\Users\\Mig\\Documents\\Thesis\\S8+\\data_set\\resize_img\\S8+_data-14.txt"

greetings()
device_img = read_image(source_image)
edit_img = device_img.copy()

with open(start_index_path, 'r')as data_file:
    for line in data_file:
        no, x, y = line.split(",")

        device_pixel_list, edit_image = plot_coordinate(device_img, edit_img, int(x), int(y), region)

        write_file(write_file_name, device_pixel_list)

        print("Finish Image", no)


write_image(plot_image, edit_img)
print("Finish -------------")