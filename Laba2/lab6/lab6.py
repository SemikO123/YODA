from tkinter import *
from math import *

root = Tk()
root.geometry('1200x600+0+0')
canv = Canvas(root, width = 1200, height = 600 ,
              bg = 'lightblue', cursor = 'pencil')
#************
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(rgb)

def line(x, y, length, angle = 0, width = 0, fill = 'black'):
    angle = radians(angle)
    x1 = x - cos(angle)*length
    y1 = y - sin(angle)*length
    canv.create_line(x,y,x1,y1, width = width, fill = fill)
    return x1,y1

def fractal_tree(x, y, length, angle = 90, color = [0,0,0], curr_deep = 1, deep =8):
    if curr_deep <= deep:
        x1,y1 = line(x,y, length, angle, width = 2, fill = rgb_to_hex(color))
        rad_angle = radians(angle)
        x2 = x - cos(rad_angle)*(length*0.7)
        y2 = y - sin(rad_angle)*(length*0.7)
        x3 = x - cos(rad_angle)*(length*0.4)
        y3 = y - sin(rad_angle)*(length*0.4)
        new_color = int(255*(curr_deep/deep))
        fractal_tree(x1, y1, length*0.7, angle+37,
                     [new_color,color[1],color[2]], curr_deep+1)
        fractal_tree(x1, y1, length*0.7, angle-37,
                     [color[0],new_color,color[2]], curr_deep+1)
        fractal_tree(x2, y2, length*0.7, angle-37,
                     [color[0],color[1],new_color], curr_deep+1)
        fractal_tree(x3, y3, length*0.7, angle+37,
                     [color[0],color[1],color[2]], curr_deep+1)
        
def half_sun(x,y):
    canv.create_arc([x-200,y-100],[x+200,y+100],start=0,
                    extent=180,outline = 'yellow', fill = 'yellow')
    for i in range(15,166,15):
        line(600,200,400, angle = i, fill = 'yellow', width = 3)

def cloud(x, y, radius):
    canv.create_oval(x + radius * 0.1, y + radius * 0.1, x - radius,
                     y + radius * 0.7, width=0, fill='white')
    canv.create_oval(x - radius * 0.1, y + radius * 0.1, x + radius,
                     y + radius * 0.7, width=0, fill='white')
    canv.create_oval(x + radius * 0.1, y - radius * 0.1, x - radius,
                     y - radius * 0.7, width=0, fill='white')
    canv.create_oval(x - radius * 0.1, y - radius * 0.1, x + radius,
                     y - radius * 0.7, width=0, fill='white')
    canv.create_oval(x - radius * 0.5, y - radius * 0.4, x - radius * 1.5,
                     y + radius * 0.4, width=0, fill='white')
    canv.create_oval(x + radius * 0.5, y - radius * 0.4, x + radius * 1.5,
                     y + radius * 0.4, width=0, fill='white')
    canv.create_oval(x - radius * 0.5, y - radius * 0.5, x + radius * 0.5,
                     y + radius * 0.5, width=0, fill='white')
    

def man(x,y,height = 400):
    width = height*0.3
    #шея
    canv.create_line(x+width*0.5,y+height*0.1,x+width*0.5,y+height*0.17, width= 2)
    #руки
    canv.create_line(x,y+height*0.17,x+width*0.25,y+height*0.41, width= 2)
    canv.create_line(x+width,y+height*0.17,x+width*0.75,y+height*0.41, width= 2)
    #ноги
    canv.create_line(x+width*0.1,y+height,x+width*0.45,y+height*0.6,width = 2)
    canv.create_line(x+width*0.9,y+height,x+width*0.55,y+height*0.6,width = 2)
    canv.create_line(x,y+height,x+width*0.1,y+height,width = 2)
    canv.create_line(x+width,y+height,x+width*0.9,y+height,width = 2)
    #голова туловище
    canv.create_oval(x+width*0.1,y,x+width*0.9,y+height*0.1, fill = 'Peach Puff')
    canv.create_oval(x+width*0.3,y+height*0.03,x+width*0.37,y+height*0.03+width*0.07)
    canv.create_oval(x+width*0.7,y+height*0.03,x+width*0.77,y+height*0.03+width*0.07)
    canv.create_line(x+width*0.5,y+height*0.07,x+width*0.7,y+height*0.07)
    canv.create_oval(x+width*0.25,y+height*0.16,x+width*0.75,y+height*0.66,
                                                             fill = 'Peach Puff')
    #знак
    canv.create_polygon([x+width*0.30,y+height*0.30],
                        [x+width*0.70,y+height*0.30],
                        [x+width*0.70,y+height*0.45],
                        [x+width*0.50,y+height*0.55],
                        [x+width*0.30,y+height*0.45], fill = 'blue')
    canv.create_line([x+width*0.65,y+height*0.33],
                      [x+width*0.35,y+height*0.33],
                      [x+width*0.35,y+height*0.38],
                      [x+width*0.65,y+height*0.38],
                      [x+width*0.65,y+height*0.45],
                      [x+width*0.35,y+height*0.45], width = 3, fill = 'red')
    
def sign(x,y,size=100):
    canv.create_oval(x,y,x+size,y+size, width = 2, fill = 'red')
    canv.create_rectangle(x+size*0.20,y+size*0.42,x+size*0.8,y+size*0.58,
                                                  width = 0, fill = 'white')
    line(x+size/2,y+size,size,-90,width = 2)

def hell_sign(x,y):
    canv.create_rectangle(x,y,x+100,y+20,fill = 'white',width = 2)
    canv.create_text(x+50,y+10, text='6 6 6',fill ='red', font='14')
    line(x+50,y+20,100,-90,width = 2)
    
    
#************

        
canv.create_rectangle(0,0,1200,200, fill = 'Sky Blue',width = 0)
canv.create_rectangle(0,200,1200,600, fill = 'Sandy Brown',width = 0)
canv.create_polygon([450,600],[750,600],[650,200],[550,200], fill = 'Dim Gray')
canv.create_polygon([585,600],[615,600],[605,200],[595,200], fill = 'white')
half_sun(600,200)
fractal_tree(900,375,90)
cloud(175,75,50)
man(100,250,280)
sign(800,350)
hell_sign(350,350)
canv.create_text(150,550, text = 'Кононенко Семён - Highway to HELL',
                 fill = 'red', font = '35')
#************
canv.pack()
root.mainloop()

