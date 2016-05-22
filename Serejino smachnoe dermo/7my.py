from tkinter import *
from math import *
from  random import *
root = Tk()


# Draw whell with lines
def whell(x, y, radius):
    canv.create_oval(x - radius, y - radius, x + radius, y + radius, width=3, fill='red')
    r = radius / sqrt(2)
    canv.create_line(x - r, y - r, x + r, y + r, width=2, fill='black')
    canv.create_line(x + r, y - r, x - r, y + r, width=2, fill='black')

def driver(x,y,height,length):
    #head
    canv.create_oval(x, y, x + length, y + height * 0.6, fill='white')

    #body
    canv.create_line(x + length / 2, y + height * 0.6, x + length / 2, y + height)

    #arms
    canv.create_line(x + length / 2, y + height * 0.6, x + length * 0.8, y + height * 0.9)
    canv.create_line(x + length / 2, y + height * 0.6, x + length * 0.2, y + height * 0.9)

    #face
    canv.create_line(x + length * 0.3, y + height * 0.2, x + length * 0.3, y + height * 0.1)
    canv.create_line(x + length * 0.7, y + height * 0.2, x + length * 0.7, y + height * 0.1)

    canv.create_oval(x + length * 0.35, y + height * 0.3, x + length * 0.7, y + height * 0.45, fill='white')

def cabine(x, y, height, length, wr):
    points = []

    #pipe
    canv.create_rectangle(x + length * 0.1, y,x + length * 0.15,y - height * 0.2,fill='brown')
    
    # main part of cabine
    points.append([x, y])
    points.append([x + length * 0.6, y])
    points.append([x + length * 0.6, y + 0.6 * height])
    points.append([x + length, y + 0.6 * height])
    points.append([x + length, y + height])
    points.append([x, y + height])
    canv.create_polygon(points, fill='green')

    #window
    canv.create_rectangle(x + length * 0.6,
                          y + height * 0.6, x + length * 0.45 ,
                          y + height * 0.3,fill='lightblue')

    #lights
    canv.create_rectangle(x + length * 0.95, y + height * 0.65,x + length,y + height * 0.7,fill='yellow')
    canv.create_rectangle(x + length * 0.95, y + height * 0.9,x + length,y + height * 0.95,fill='yellow')
    canv.create_rectangle(x, y + height * 0.9,x + length * 0.05,y + height * 0.95,fill='red')
    canv.create_rectangle(x, y + height * 0.05,x + length * 0.05,y + height * 0.1,fill='red')

    #door
    canv.create_rectangle(x + length * 0.15, y + height, x + length * 0.4 ,y + height * 0.4,fill='brown', width = 0)
    canv.create_rectangle(x + length * 0.35, y + height * 0.7, x + length * 0.38 ,y + height * 0.77,fill='black', width = 0)
    
    #connector
    canv.create_line(x, y + height * 0.8, x - length * 0.3, y + height * 0.8,width = 10)

    #driver
    driver(x + length * 0.48, y + height * 0.4,height * 0.2, length * 0.1)

    #wheels
    whell(x + length * 0.15, y + height + length * 0.1, wr)
    whell(x + length * 0.8, y + height + length * 0.1, wr)

def trailer(x, y, height, length ,wr):
    
    # main part of trailer
    canv.create_rectangle(x, y, x + length,y + height,fill='red')
    canv.create_text(x * 2.4,y * 1.25,text = 'КОКА - КОЛА' ,
                     fill = 'white', anchor = 'w', justify = 'center',
                     font = 'arial 20')
    whell(x + length * 0.05, y + height + length * 0.05, wr)
    whell(x + length * 0.15, y + height + length * 0.05, wr)
    whell(x + length * 0.9, y + height + length * 0.05, wr)


def sun(x, y, radius):
    koef = 1.8
    for i in range(0, 180, 20):
        rads = i * 2 * pi / 360
        rx = (radius * koef) * sin(rads)
        ry = (radius * koef) * cos(rads)
        canv.create_line(x - rx, y - ry, x + rx, y + ry, width=2, fill='yellow')
        
    for i in range(0, 180, 20):
        rads = i * 2 * pi / 360
        rx = (radius * koef * 0.65) * sin(rads)
        ry = (radius * koef * 0.65) * cos(rads)
        canv.create_line(x - rx, y - ry, x + rx, y + ry, width=2, fill='lightblue')
    canv.create_oval(x - radius, y - radius, x + radius, y + radius, width=0, fill='yellow')


def cloud(x, y, radius):
    canv.create_oval(x + radius * 0.1, y + radius * 0.1, x - radius, y + radius * 0.7, width=0, fill='gray')
    canv.create_oval(x - radius * 0.1, y + radius * 0.1, x + radius, y + radius * 0.7, width=0, fill='gray')
    canv.create_oval(x + radius * 0.1, y - radius * 0.1, x - radius, y - radius * 0.7, width=0, fill='gray')
    canv.create_oval(x - radius * 0.1, y - radius * 0.1, x + radius, y - radius * 0.7, width=0, fill='gray')
    canv.create_oval(x - radius * 0.5, y - radius * 0.4, x - radius * 1.5, y + radius * 0.4, width=0, fill='gray')
    canv.create_oval(x + radius * 0.5, y - radius * 0.4, x + radius * 1.5, y + radius * 0.4, width=0, fill='gray')
    canv.create_oval(x - radius * 0.5, y - radius * 0.5, x + radius * 0.5, y + radius * 0.5, width=0, fill='gray')

def ufo(x,y,height,length):
    canv.create_oval(x + length / 4, y, x + length * 3 / 4, y + height /4, width=0, fill='blue')
    canv.create_oval(x, y + height / 16, x + length, y + height*3/16, width=0, fill='blue')
    points = []
    points.append([x + length/2, y + height * 5 / 16])
    points.append([x + length, y + height])
    points.append([x, y + height])
    canv.create_polygon(points, fill='lightgreen')
    
def text(x,y):
    canv.create_text(x, y, text = 'Шофер - Говязин Сергей' ,
                     fill = 'blue', anchor = 'w', justify = 'center',
                     font = 'arial 30')

canv = Canvas(root, width=1000, height=700, bg='lightblue', cursor='pencil')

sun(200,100,50)
cloud(700,50,50)
cabine(600,300,150,200,20)
trailer(100,300,150,450,20)
ufo(500,100,150,100)
text(300,600)


canv.pack()
root.mainloop()
