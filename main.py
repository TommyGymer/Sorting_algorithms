import colorsys #values between 0 and 1
import random
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import time
import cv2

steps = 500
width = 960

count = 8
height = 480

def _photo_image(image: np.ndarray):
    height, width = image.shape[:2]
    ppm_header = f'P6 {width} {height} 255 '.encode()
    data = ppm_header + cv2.cvtColor(image, cv2.COLOR_BGR2RGB).tobytes()
    return tk.PhotoImage(width=width, height=height, data=data, format='PPM')

class Sort():
    items = []

    def __init__(self):
        for i in range(steps):
            self.items.append(i/steps)
        self.shuffle_items()
        #print(self.items)
        
    def shuffle_items(self):
        random.shuffle(self.items)

class BubbleSort(Sort):
    i = 0
    def sort(self):
        if self.i >= len(self.items) - 1:
            self.i = 0
            self.sort()
        elif self.items[self.i] > self.items[self.i + 1]:
            tmp = self.items[self.i]
            self.items[self.i] = self.items[self.i + 1]
            self.items[self.i + 1] = tmp
        

test = BubbleSort()


window = Tk()
window.geometry(str(width) + "x" + str(height))
#window.configure(background='blue')

a = np.array(test.items)

pain = [(int(255*a[int(steps*(x/width))]), 255, 255) for x in range(width)]
asdf = [pain for i in range(height)]

img = Image.fromarray(np.array(asdf, dtype=np.uint8), mode="HSV")

nande = ImageTk.PhotoImage(img)

canvas = Canvas(window, bg='grey', width=width, height=height)
canvas.pack(fill="both", expand="yes")

canvas.create_image(width/2, height/2, image=nande, state=NORMAL)
canvas.image = img

#panel.pack(side="top", fill="both", expand="yes")

while True:
    window.update_idletasks()
    window.update()

    t0 = time.time()
    test.sort()
    print(f"Sort: {time.time() - t0}")
    a = np.array(test.items)

    t0 = time.time()
    pain = [(int(255*a[int(steps*(x/width))]), 255, 255) for x in range(width)]
    asdf = [pain for i in range(height)]
    print(f"Image: {time.time() - t0}")

    t0 = time.time() #this is taking most of the time; between 0.2 and 0.3 seconds
    img = Image.fromarray(np.array(asdf, dtype=np.uint8), mode="HSV")
    print(f"From array: {time.time() - t0}")

    t0 = time.time()
    #nande = ImageTk.PhotoImage(img)
    nande = _photo_image(img)
    print(f"Photo: {time.time() - t0}")

    t0 = time.time()
    canvas.delete("all")
    canvas.create_image(width/2, height/2, image=nande, state=NORMAL)
    canvas.image = img
    print(f"Display: {time.time() - t0}")