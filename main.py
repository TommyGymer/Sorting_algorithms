import colorsys #values between 0 and 1
import random
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import time
import cv2
import copy
import os

steps = 32
width = 960

count = 8
height = 480

make_gif = False

#convert numpy array directly to PPM format for tkinter to read
def _photo_image(image: np.ndarray):
    height, width = image.shape[:2]
    ppm_header = f'P6 {width} {height} 255 '.encode()
    data = ppm_header + cv2.cvtColor(image, cv2.COLOR_HSV2RGB).tobytes()
    return ImageTk.PhotoImage(width=width, height=height, data=data, format='PPM')

class Sort():
    items = []

    def __init__(self):
        for i in range(steps):
            self.items.append(i/(1.7*steps))
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
            tmp = copy.copy(self.items[self.i])
            self.items[self.i] = self.items[self.i + 1]
            self.items[self.i + 1] = tmp
        else:
            self.i += 1
            self.sort()
        if self.items == copy.copy(self.items).sort():
            return 1
        else:
            return 0

class QuickSort(Sort):
    i = 0
    def sort(self):
        i += 1

test = BubbleSort()

window = Tk()
window.geometry(str(width) + "x" + str(height))
#window.configure(background='blue')

img_num = 0

a = np.array([int(255*test.items[int(steps*(x/width))]) for x in range(width)])
b = np.linspace(255, 255, num=len(a))
l = np.concatenate((a,b,b), axis=0).reshape(3, width).T
jkl = np.swapaxes(np.tile(l, height).reshape(width, height, 3), 0, 1)

img = np.array(jkl, dtype=np.uint8)
nande = _photo_image(img)

if make_gif:
    cv2.imwrite(os.path.join("C:\\Users\\Tom\\Pictures\\sorting", str(img_num) + ".jpg"), cv2.cvtColor(img, cv2.COLOR_HSV2RGB))
    img_num += 1

canvas = Canvas(window, bg='grey', width=width, height=height)
canvas.pack(fill="both", expand="yes")

canvas.create_image(width/2, height/2, image=nande, state=NORMAL)
canvas.image = img

#panel.pack(side="top", fill="both", expand="yes")
while True:
    window.update_idletasks()
    window.update()
    
    if test.sort():
        break
    
    a = np.array([int(255*test.items[int(steps*(x/width))]) for x in range(width)])
    b = np.linspace(255, 255, num=len(a))
    l = np.concatenate((a,b,b), axis=0).reshape(3, width).T
    jkl = np.swapaxes(np.tile(l, height).reshape(width, height, 3), 0, 1)
    
    img = np.array(jkl, dtype=np.uint8)
    nande = _photo_image(img)

    if make_gif:
        cv2.imwrite(os.path.join("C:\\Users\\Tom\\Pictures\\sorting", str(img_num) + ".jpg"), cv2.cvtColor(img, cv2.COLOR_HSV2RGB))
        img_num += 1

    canvas.delete("all")
    canvas.create_image(width/2, height/2, image=nande, state=NORMAL)
    canvas.image = img