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
        #self.shuffle_items()
        #print(self.items)
        
    def shuffle_items(self):
        random.shuffle(self.items)

test = Sort()


window = Tk()
window.geometry(str(width) + "x" + str(height))
#window.configure(background='blue')

#img = Image.open("bean_r.png")
#img = Image.open("garaph.jpg")
#
#img.show()

#print(np.asarray(img))

a = np.array(Sort.items)
b = np.ones(len(Sort.items))

pain = []

for i in range(width):
    paintemp = []
    for j in range(height):
        paintemp.append([a[int((j*steps)/width)], 1, 1])
    pain.append(paintemp)

print(np.array(pain))

#print(np.vstack((a, b , b)).T)

#print(np.block([np.flip(np.array(Sort.items), 1), np.ones((len(Sort.items),1)), np.ones((len(Sort.items),1))]))

#panel = Label(window, image = ImageTk.PhotoImage(Image.fromarray(np.vstack((a, b , b)).T, mode="HSV")))
#panel = Label(window, image = ImageTk.PhotoImage(img))

#print(np.array((np.vstack((a, b , b)).T, np.vstack((a, b , b)).T)))
#img = Image.fromarray(np.array((np.vstack((a, b , b)).T, np.vstack((a, b , b)).T)), mode="HSV").resize((width, height))
img = Image.fromarray(np.array(pain), mode="HSV").rotate(90)

nande = ImageTk.PhotoImage(img)

canvas = Canvas(window, bg='grey', width=width, height=height)
canvas.pack(fill="both", expand="yes")

canvas.create_image(width/2, height/2, image=nande, state=NORMAL)
canvas.image = img

#panel.pack(side="top", fill="both", expand="yes")

window.mainloop()