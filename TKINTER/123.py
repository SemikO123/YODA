from tkinter import *
import tkinter.messagebox as box

def gyy():
    window = Tk()
    frame = Frame(window, bg = 'blue')
    entry = Entry(frame)

    window.title('Fpfpfpfp')
    window.configure(bg = 'purple')
    label_1 = Label(window,text = 'mazafaka')
    label_2 = Label(window, text = 'bitch')

    label_1.pack(side = RIGHT, padx = 150, pady = 20)
    label_2.pack(side = LEFT, padx = 150, pady = 20)

    listbox = Listbox(frame, height = 5)
    for i in range(5):
        listbox.insert(i,i)

    kniga = StringVar()
    radio_1 = Radiobutton(frame, text = ' mouse', variable = kniga, value = '0')
    radio_2 = Radiobutton(frame, text = ' cat', variable = kniga, value = '1')
    radio_3 = Radiobutton(frame, text = ' dog', variable = kniga, value = '2')

    def chain():
        box.showinfo('Пищевая цепь','Место'+kniga.get())

    def listok():
        box.showinfo('Выбираем','В квадратик'+ str(listbox.get(listbox.curselection())**2))

    def tog():
        gyyt();

    def razgovor():
        otvet = box.askquestion('mazafaka?','отвечай, бич!')
        if otvet == 'yes' :
            box.showinfo('ублюдок','согласен...')
        else:
            box.showinfo('не ублюдок','ура)))')
        otvet = box.askyesno('asdasd','ergerherh')
        print(otvet)
        

    def okoshko():
        ololo = entry.get()
        ololo= ololo.upper()
        box.showinfo('ololo', ololo)

    alalal = Button(frame, text = 'knopka', command = chain)

    kvadr = Button(frame, text= 'vozvodi', bg = 'white', command = listok)


    vvodik = Button(frame, text = 'делай, брат', bg = '#A6A6A6', command = okoshko)



    perekl = Button(window, text = 'CCH', command = tog)

    zakritie = Button(window, text = 'ЗАкрываем окнище ипаное', bg = 'cyan', command = exit)

    poboltaem = Button(window, text = 'Давай, епт!', bg = 'cyan', command = razgovor)

    zakritie.pack(padx = 228, pady = 113)
    perekl.pack()
    poboltaem.pack( pady = 50)
    vvodik.pack(pady = 20)
    entry.pack(pady = 20)
    listbox.pack(pady = 20)
    kvadr.pack(pady = 20)

    radio_1.pack(side = RIGHT,ipadx = 100)
    radio_2.pack(side = RIGHT,ipadx= 100)
    radio_3.pack(side = RIGHT)
    alalal.pack(side = RIGHT)
    frame.pack(padx = 100,pady = 1)
    window.mainloop()

def gyyt():
    window = Tk()
    frame = Frame(window, bg = 'red')
    entry = Entry(frame)

    window.title('Fpfpfpfp')
    window.configure(bg = 'purple')
    label_1 = Label(window,text = 'mazafaka')
    label_2 = Label(window, text = 'bitch')

    label_1.pack(side = RIGHT, padx = 150, pady = 20)
    label_2.pack(side = LEFT, padx = 150, pady = 20)

    listbox = Listbox(frame, height = 5)
    for i in range(5):
        listbox.insert(i,i)

    kniga = StringVar()
    radio_1 = Radiobutton(frame, text = ' mouse', variable = kniga, value = '0')
    radio_2 = Radiobutton(frame, text = ' cat', variable = kniga, value = '1')
    radio_3 = Radiobutton(frame, text = ' dog', variable = kniga, value = '2')

    def chain():
        box.showinfo('Пищевая цепь','Место'+kniga.get())

    def listok():
        box.showinfo('Выбираем','В квадратик'+ str(listbox.get(listbox.curselection())**2))

    def tog():
        gyy();

    def razgovor():
        otvet = box.askquestion('mazafaka?','отвечай, бич!')
        if otvet == 'yes' :
            box.showinfo('ублюдок','согласен...')
        else:
            box.showinfo('не ублюдок','ура)))')
        otvet = box.askyesno('asdasd','ergerherh')
        print(otvet)
        

    def okoshko():
        ololo = entry.get()
        ololo= ololo.upper()
        box.showinfo('ololo', ololo)

    alalal = Button(frame, text = 'knopka', command = chain)

    kvadr = Button(frame, text= 'vozvodi', bg = 'white', command = listok)


    vvodik = Button(frame, text = 'делай, брат', bg = '#A6A6A6', command = okoshko)



    perekl = Button(window, text = 'CCH', command = tog)

    zakritie = Button(window, text = 'ЗАкрываем окнище ипаное', bg = 'cyan', command = exit)

    poboltaem = Button(window, text = 'Давай, епт!', bg = 'cyan', command = razgovor)

    zakritie.pack(padx = 228, pady = 113)
    perekl.pack()
    poboltaem.pack( pady = 50)
    vvodik.pack(pady = 20)
    entry.pack(pady = 20)
    listbox.pack(pady = 20)
    kvadr.pack(pady = 20)

    radio_1.pack(side = RIGHT,ipadx = 100)
    radio_2.pack(side = RIGHT,ipadx= 100)
    radio_3.pack(side = RIGHT)
    alalal.pack(side = RIGHT)
    frame.pack(padx = 100,pady = 1)
    window.mainloop()
gyy()
