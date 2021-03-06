from tkinter import *

root = Tk()
canv = Canvas(root, width=1000, height=700, bg='lightblue', cursor='pencil')

canv.create_oval(100, 200, 600, 700, fill='brown', outline = 'black',width = 10)

points = []
points.append([50, 200])
points.append([50, 500])
points.append([650, 500])
points.append([650, 100])
canv.create_polygon(points, fill='lightblue')


points = []
points.append([40, 500])
points.append([300, 450])
points.append([695, 500])
points.append([300, 550])
canv.create_polygon(points, fill='brown',smooth = 1, outline = 'black',width = 10)

canv.create_oval(220, 550, 270, 600, fill='blue')

canv.create_oval(350, 550, 400, 600, fill='blue')

canv.create_oval(450, 550, 500, 600, fill='blue')

points = []
points.append([350, 100])
points.append([200, 400])
points.append([350, 420])
canv.create_polygon(points, fill='white')

points = []
points.append([350, 100])
points.append([400, 100])
points.append([380, 120])
points.append([400, 140])
points.append([350, 140])
canv.create_polygon(points, fill='red')


canv.create_line(350,500,350,100,width = 10)


canv.create_oval(475, 350, 525, 400, fill='lightblue', outline = 'black',width = 5)
canv.create_line(500,500,500,300,width = 5)
canv.create_line(450,375,550,375,width = 5)
canv.create_line(450,325,550,425,width = 5)
canv.create_line(450,425,550,325,width = 5)


canv.create_oval(170, 550, 200, 580, fill='black')
canv.create_line(185,580,200,600,width = 5)
canv.create_line(185,580,170,600,width = 5)

canv.pack()
root.mainloop()
