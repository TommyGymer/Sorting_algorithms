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
    ref = []
    done = False

    def __init__(self):
        for i in range(steps):
            self.items.append(i/(1.5*steps))
        self.shuffle_items()
        #print(self.items)
        self.ref = copy.copy(self.items)
        self.ref.sort()
        
    def shuffle_items(self):
        random.shuffle(self.items)
        self.done = False

    def genImgArr(self):
        data = np.array([int(255*self.items[int(steps*(x/width))]) for x in range(width)])
        fill = np.linspace(255, 255, num=len(data))
        row = np.concatenate((data,fill,fill), axis=0).reshape(3, width).T
        return np.swapaxes(np.tile(row, height).reshape(width, height, 3), 0, 1)

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
        if self.items == self.ref:
            self.done = True
            return 1
        else:
            return 0

class InsertionSort(Sort):
    i = 0
    j = 0
    prev = 0
    def sort(self):
        #print(f"{self.i}, {self.j}, {self.prev}")
        if self.j == 0 or self.i == 0:
            self.i += 1
            self.prev = self.i
            self.j = self.i
        self.j -= 1
        if self.items[self.i] < self.items[self.j]:
            tmp = copy.copy(self.items[self.i])
            self.items[self.i] = self.items[self.j]
            self.items[self.j] = tmp
            self.i -= 1
        else:
            self.i = self.prev
            self.j = 0
        if self.items == self.ref:
            self.done = True
            return 1
        else:
            return 0

class QuickSort(Sort):
    i = 0
    pivot = -1
    small = 0
    large = 0

    #Add each list along with start and end index into self.items
    #Use of a temp-stack for the next depth might be necessary
    #Pick a pivot and process each of the lists within the stack
    #Then add the left and right of each of these lists to the temp-stack
    #Once the current stack is empty, swap the stacks

    def sort(self):
        if self.items[self.i] < self.items[self.pivot]:
            tmp = copy.copy(self.items[self.small])
            self.items[self.small] = self.items[self.i]
            self.items[self.i] = tmp
            self.small += 1
        elif self.items[self.i] > self.items[self.pivot]:
            tmp = copy.copy(self.items[self.small + self.large])
            self.items[self.small + self.large] = self.items[self.i]
            self.items[self.i] = tmp
            self.large += 1
        self.i += 1
        if self.i == len(self.items):
            for k in range(self.small, self.small + self.large - 1):
                tmp = copy.copy(self.items[k+1])
                self.items[k+1] = self.items[k]
                self.items[k] = tmp
            #need to pick a new pivot
            self.done = True
        
        if self.items == self.ref:
            self.done = True
            return 1
        else:
            return 0

test = QuickSort()

window = Tk()
window.geometry(str(width) + "x" + str(height))
#window.configure(background='blue')

img_num = 0

img = np.array(test.genImgArr(), dtype=np.uint8)
nande = _photo_image(img)

if make_gif:
    cv2.imwrite(os.path.join(".\\output", str(img_num) + ".jpg"), cv2.cvtColor(img, cv2.COLOR_HSV2RGB))
    img_num += 1

canvas = Canvas(window, bg='grey', width=width, height=height)
canvas.pack(fill="both", expand="yes")

canvas.create_image(width/2, height/2, image=nande, state=NORMAL)
canvas.image = img

#panel.pack(side="top", fill="both", expand="yes")

def close_window():
    global running
    running = False

window.protocol("WM_DELETE_WINDOW", close_window())

running = True

while running:
    try:
        window.update()
        if not test.done:
            test.sort()
            
            img = np.array(test.genImgArr(), dtype=np.uint8)
            nande = _photo_image(img)

            if make_gif:
                cv2.imwrite(os.path.join(".\\output", str(img_num) + ".jpg"), cv2.cvtColor(img, cv2.COLOR_HSV2RGB))
                img_num += 1

            canvas.delete("all")
            canvas.create_image(width/2, height/2, image=nande, state=NORMAL)
            canvas.image = img
    except Exception as e:
        print(e)
        break