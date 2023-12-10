from tkinter import *
import random
import time
from PIL import Image, ImageTk

def get_random_bro_image():
    return ImageTk.PhotoImage(Image.open(random.choice(['images/b1.png', 'images/b2.png', 'images/b3.png', 'images/b4.png', 'images/b5.png', 'images/b6.png'])))

def change_images(event):
    for _ in range(20):
        lab1['image'] = get_random_bro_image()
        lab2['image'] = get_random_bro_image()
        root.update()
        time.sleep(0.15)

root = Tk()
root.geometry('400x200')
root.title('Let\'s play dice! Click to roll')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='images/icon.png'))

background_image = PhotoImage(file='images/background.png')
Label(root, image=background_image).pack()

lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)

lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

root.bind('<1>', change_images)
change_images('event')

root.mainloop()
