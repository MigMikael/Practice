from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2


count = 1
click_count = 1
img_one_point = []
img_two_point = []


def select_image():
    global path
    global image_one
    global image_two
    global cv2_image_one
    global cv2_image_two
    global count

    path = filedialog.askopenfilename()
    print(path)
    if len(path) > 0:
        if count % 2 != 0:
            cv2_image_one = cv2.imread(path)
            image_one = Image.fromarray(cv2_image_one)
            image_one = ImageTk.PhotoImage(image_one)

            print(image_one.width())
            print(image_one.height())
            canvas1.pack_forget()
            canvas1.create_image(image_one.width()/2, image_one.height()/2, anchor=CENTER, image=image_one)
            canvas1.config(scrollregion=(0, 0, image_one.width(), image_one.height()))

            hbar1 = Scrollbar(canvas1, orient=HORIZONTAL)
            hbar1.pack(side=BOTTOM, fill=X)
            hbar1.config(command=canvas1.xview)

            vbar1 = Scrollbar(canvas1, orient=VERTICAL)
            vbar1.pack(side=RIGHT, fill=Y)
            vbar1.config(command=canvas1.yview)

            canvas1.config(width=400, height=400)
            canvas1.config(xscrollcommand=hbar1.set, yscrollcommand=vbar1.set)
            canvas1.pack(side=LEFT, expand=True, fill=BOTH)
        else:
            cv2_image_two = cv2.imread(path)
            image_two = Image.fromarray(cv2_image_two)
            image_two = ImageTk.PhotoImage(image_two)

            print(image_two.width())
            print(image_two.height())
            canvas2.pack_forget()
            canvas2.create_image(image_two.width() / 2, image_two.height() / 2, anchor=CENTER, image=image_one)
            canvas2.config(scrollregion=(0, 0, image_two.width(), image_two.height()))

            hbar2 = Scrollbar(canvas2, orient=HORIZONTAL)
            hbar2.pack(side=BOTTOM, fill=X)
            hbar2.config(command=canvas2.xview)

            vbar2 = Scrollbar(canvas2, orient=VERTICAL)
            vbar2.pack(side=RIGHT, fill=Y)
            vbar2.config(command=canvas2.yview)

            canvas2.config(width=400, height=400)
            canvas2.config(xscrollcommand=hbar2.set, yscrollcommand=vbar2.set)
            canvas2.pack(side=LEFT, expand=True, fill=BOTH)
        print(count)
        count += 1


def on_mouse_down(event):
    global image_one
    global image_two
    global cv2_image_one
    global cv2_image_two
    global click_count
    cord_x = event.x
    cord_y = event.y
    print("frame coordinates : {}, {}".format(cord_x, cord_y))
    # print("root coordinates : {}, {}".format(event.x_root, event.y_root))
    if click_count % 2 != 0:
        img_one_point.append([cord_x, cord_y])
        print("image 1 pixel : {}".format(cv2_image_one[cord_x, cord_y]))
    else:
        img_two_point.append([cord_x, cord_y])
        print("image 2 pixel : {}".format(cv2_image_two[cord_x, cord_y]))

    print("##### click : {}".format(click_count))
    click_count += 1


def clear_image():
    global count
    count = 1
    canvas1.delete('all')
    canvas2.delete('all')
    for widget in canvas1.winfo_children():
        widget.destroy()
    for widget in canvas2.winfo_children():
        widget.destroy()


def save_data():
    global path
    #print(img_one_point)
    #print(img_two_point)
    word = path.split('/')
    last_word = word[-1]
    des_path = path.replace(last_word, '')

    for cord in img_one_point:
        x = cord[0]
        y = cord[1]
        print("image 1 pixel : {}".format(cv2_image_one[x, y]))
        cv2_image_one[x:x+5, y:y+5] = 0
        cv2_image_one[x, y] = 255

    cv2.imwrite(des_path + '/image_one.jpg', cv2_image_one)
    print("Finish")


root = Tk()
root.state('zoomed')

canvas1 = Canvas(root, bg='blue', width=400, height=400)
canvas1.pack(side='left')
canvas1.bind("<1>", on_mouse_down)


canvas2 = Canvas(root, bg='blue', width=400, height=400)
canvas2.pack(side='right')
canvas2.bind("<1>", on_mouse_down)


btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="top", padx="10", pady="10")


clear_btn = Button(root, text="SAVE", command=save_data)
clear_btn.pack(side="top", padx="10", pady="10")

root.mainloop()
