import colorsys #values between 0 and 1
import random
from tkinter import *
from PIL import ImageTk, Image
import numpy as np

steps = 500
width = 960

count = 8
height = 480

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

    #test.sort()
    #a = np.array(test.items)

    #img = Image.new("HSV", (width, height))

    #this is tool slow
    #for i in range(width):
    #    for j in range(height):
    #        img.putpixel((i, j), (int(255*(a[int((i * steps)/width)])), 255, 255))

    #nande = ImageTk.PhotoImage(img)
    #canvas.delete("all")
    #canvas.create_image(width/2, height/2, image=nande, state=NORMAL)
    #canvas.image = img