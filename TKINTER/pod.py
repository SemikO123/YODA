
from tkinter import *

# Lable, title
'''
root = Tk()
root.title('Label')
label = Label(root, text = 'Hello!')
label.pack(padx = 200, pady = 200)
root.mainloop() 
'''

# Button example (смена цвета кнопочки)
'''
window = Tk()
btn_end = Button(window, text = 'aaa', command = exit)
def tog():  # Функция цвета
    if window.cget('bg') == 'yellow':
        window.configure(bg = 'green')
    else:
        window.configure(bg = 'yellow')
btn_tog = Button(window, text = 'bbb', command = tog)

#btn_end.pack(padx = 150, pady = 20)
btn_end.place(x = 20, y = 20, height = 15)  # по координаткам
btn_tog.pack(padx = 150, pady = 20)
window.mainloop()
'''

# Вывод сообщения (messagebox)
'''
import tkinter.messagebox as box
window = Tk()
def dialog():
    variant = box.askyesno('Блок сообщения', 'Продолжать')
    if variant == 1:
        box.showinfo('Блок Да', 'Продолжение...')
    else:
        box.showwarning('Блок Нет', 'Выход')
btn = Button(window, text = 'Нажать', command = dialog)
btn.pack(padx = 150, pady = 50)
window.mainloop()
'''

# Entry - виджет (ввод данных)
'''
import tkinter.messagebox as box
window = Tk()
frame = Frame(window)
entry = Entry(frame)
def dialog():
    box.showinfo('Приглашение', 'Сдавать экзамен в сентябре '+entry.get())
btn = Button(frame, text = 'Введите фамилию', command = dialog)
btn.pack(side = RIGHT, padx = 10)
entry.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)
window.mainloop()
'''



# Создание фрейма
import tkinter.messagebox as box
window = Tk()
frame = Frame(window)

# Пример на список - listbox
'''
# Фрейм
listbox = Listbox(frame)
listbox.insert('1', 'Python')
listbox.insert('2', 'Java')
listbox.insert('3', 'Ada')
listbox.insert('4', 'Delphi')
listbox.insert('5', 'C')

def dialog():
    box.showinfo('Список для выбора', 'Ваш выбор язык: '+listbox.get(listbox.curselection()))
btn = Button(frame, text = 'Выбор', command = dialog)
btn.pack(side = RIGHT, padx = 5)
listbox.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)
window.mainloop()
'''

# Создание переключателя - radiobutton
'''
book = StringVar()
radio_1 = Radiobutton(frame, text = 'Mark 1', variable = book, value = '1952')
radio_2 = Radiobutton(frame, text = 'Noy', variable = book, value = '1552')
radio_3 = Radiobutton(frame, text = 'Nemark', variable = book, value = '1772')
radio_4 = Radiobutton(frame, text = 'Hey', variable = book, value = '1762')
radio_5 = Radiobutton(frame, text = 'Purpur', variable = book, value = '1992')
radio_1.select()
def dialog():
    box.showinfo('Selection', 'Выбор: \n' + book.get())
btn = Button(frame, text = ' Выбрано ', command = dialog)
btn.pack(side = RIGHT, padx = 5)
radio_1.pack(side = LEFT)
radio_2.pack(side = LEFT)
radio_3.pack(side = LEFT)
radio_4.pack(side = LEFT)
radio_5.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)
window.mainloop()
'''

# CheckButtton

var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
var_5 = IntVar()
book_1 = Checkbutton(frame, text = 'Fortran', variable = var_1, onvalue = 1, offvalue = 0)
book_1 = Checkbutton(frame, text = 'Basic', variable = var_1, onvalue = 1, offvalue = 0)
book_1 = Checkbutton(frame, text = 'Ada', variable = var_1, onvalue = 1, offvalue = 0)
book_1 = Checkbutton(frame, text = 'Python', variable = var_1, onvalue = 1, offvalue = 0)
book_1 = Checkbutton(frame, text = 'Swift', variable = var_1, onvalue = 1, offvalue = 0)
def dialog():
    str = 'Выбор языка: '
    if var_1.get() == 1:
        str += '\n 1954'
    if var_2.get() == 1:
        str += '\n 1964'
    if var_3.get() == 1:
        str += '\n 1983'
    if var_4.get() == 1:
        str += '\n 1991'
    else:
        str += '\n 2014'
frame.pack(padx = 30, pady = 30)
window.mainloop()
