import cv2
from tkinter import *
import numpy as np
from tkinter import filedialog


img1_cord = []
img2_cord = []
region = 7
total_click = 3
click_count = 0.0


# mouse callback function
def draw_rectangle1(event, x, y, flags, param):
    global click_count
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img1, (x, y), (x + region, y + region), (0, 255, 0), 1)
        img1_cord.append([x, y])
        print(img1[x, y])
        print(x, y)
        click_count += 0.5
        print("####### click " + str(click_count))
        click_value.set(str(click_count))


# mouse callback function
def draw_rectangle2(event, x, y, flags, param):
    global click_count
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img2, (x, y), (x + region, y + region), (0, 255, 0), 1)
        img2_cord.append([x, y])
        print(img2[x, y])
        print(x, y)
        click_count += 0.5
        print("####### click " + str(click_count))
        click_value.set(str(click_count))


def select_image():
    global img1
    global img2
    global path
    path = filedialog.askdirectory()
    print(path)
    if len(path) > 0:
        # Create a black image, a window and bind the function to window
        img1 = cv2.imread(path + '/img1.jpg')
        img2 = cv2.imread(path + '/img2.jpg')

        cv2.namedWindow('image1', cv2.WND_PROP_FULLSCREEN)
        cv2.setMouseCallback('image1', draw_rectangle1)

        cv2.namedWindow('image2', cv2.WND_PROP_FULLSCREEN)
        cv2.setMouseCallback('image2', draw_rectangle2)

        while (True):
            cv2.imshow('image1', img1)
            cv2.imshow('image2', img2)
            if cv2.waitKey(20) & 0xFF == 27 or click_count == total_click:
                '''
                for cord in img1_cord:
                    print("img 1 cord : " + str(cord[0]) + " " + str(cord[1]))
                    print(img1[cord[0], cord[1]])
                for cord in img2_cord:
                    print("img 2 cord : " + str(cord[0]) + " " + str(cord[1]))
                    print(img2[cord[0], cord[1]])
                '''
                break
        cv2.destroyAllWindows()


def save_data():
    global path

    the_img1 = cv2.imread(path + '/img1.jpg')
    the_img2 = cv2.imread(path + '/img2.jpg')

    for num in range(total_click):
        print(num)
        x1 = img1_cord[num][0]
        y1 = img1_cord[num][1]
        print("image 1 pixel : {}".format(the_img1[x1, y1]))
        tiny_crop_one = the_img1[y1:y1 + region, x1:x1 + region]
        cv2.imwrite(path + '/img1_tiny_crop_' + str(num) + '.jpg', tiny_crop_one)
        print(tiny_crop_one.shape)
        data_one = tiny_crop_one.ravel()
        data_one = data_one.astype(np.int64)

        data_set_one = ["|labels "]
        for i in range(data_one.shape[0]):
            data_set_one.append(str(data_one[i]) + " ")

        x2 = img2_cord[num][0]
        y2 = img2_cord[num][1]
        print("image 2 pixel : {}".format(the_img2[x2, y2]))
        tiny_crop_two = the_img2[y2:y2 + region, x2:x2 + region]
        cv2.imwrite(path + '/img2_tiny_crop_' + str(num) + '.jpg', tiny_crop_two)
        print(tiny_crop_two.shape)
        data_two = tiny_crop_two.ravel()
        data_two = data_two.astype(np.int64)

        data_set_two = ["|features "]
        for i in range(data_two.shape[0]):
            data_set_two.append(str(data_two[i]) + " ")
        data_set_two.append('\n')

        if num == 0:
            with open(path + '/train-data.txt', 'w') as outfile:
                for data_line in data_set_one:
                    outfile.write(data_line)
                for data_line in data_set_two:
                    outfile.write(data_line)
        else:
            with open(path + '/train-data.txt', 'a') as outfile:
                for data_line in data_set_one:
                    outfile.write(data_line)
                for data_line in data_set_two:
                    outfile.write(data_line)

        print(data_set_one)
        print(len(data_set_one))

        print(data_set_two)
        print(len(data_set_two))

    cv2.imwrite(path + '/img1_edit.jpg', img1)
    cv2.imwrite(path + '/img2_edit.jpg', img2)


def quit_program():
    root.quit()


root = Tk()
root.title('Region Picker')
root.state('zoomed')


control_frm = Frame(root, bg='blue')
control_frm.pack(side='top')

reset_btn = Button(control_frm, text="QUIT", command=quit_program)
reset_btn.pack(side='left', padx="10", pady="10")

select_btn = Button(control_frm, text="Select an image", command=select_image)
select_btn.pack(side='left', padx="100", pady="10")

save_btn = Button(control_frm, text="SAVE", command=save_data)
save_btn.pack(side='left', padx="10", pady="10")


click_value = StringVar()
click_label = Label(root, textvariable=click_value, bg='red')
click_value.set('0')
click_label.pack(side='top')


left_frame = Frame(root)
left_frame.pack(side='left')

first_frame_name = Label(left_frame, text="Image 1 Position")
first_frame_name.pack(side='top')

first_frame = Frame(left_frame, bg='#e0e0e0', width=600, height=500)
first_frame.pack(side='left')


right_frame = Frame(root)
right_frame.pack(side='right')

second_frame_name = Label(right_frame, text="Image 2 Position")
second_frame_name.pack(side='top')

second_frame = Frame(right_frame, bg='#e0e0e0', width=600, height=500)
second_frame.pack(side='right')


root.mainloop()