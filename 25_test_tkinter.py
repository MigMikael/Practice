from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2


def select_image():
    global panelA, panelB

    path = filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path)

        # convert image to PIL format
        image = Image.fromarray(image)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)

    if panelA is None or panelB is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side='left', padx=10, pady=10)

        panelB = Label(image=image)
        panelB.image = image
        panelB.pack(side='right', padx=10, pady=10)
    else:
        # update the pannel
        panelA.configure(image=image)
        panelB.configure(image=image)
        panelA.image = image
        panelB.image = image


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


root = Tk()
panelA = None
panelB = None

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

root.bind('<Motion>', motion)
root.mainloop()