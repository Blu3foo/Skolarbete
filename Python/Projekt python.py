from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import time
from threading import Thread
root = Tk()
root.minsize(900, 600)
root.maxsize(1000, 900)


global count
count = 0


def donothing():
    tkinter.messagebox.showinfo('Beta', 'This funktion is yet to be implemented')


def newfile():
    global count
    answer = tkinter.messagebox.askquestion('Create new file', 'Would you like to save the current file?')
    if answer == 'yes':
        saveasfile()
    elif answer == 'no':
        pass
    text.delete(1.0, END)
    text.insert(INSERT, 'Get to writing!')
    count = 0



# Funktion för att öppna existerande textfile
def fileopen():
    of = filedialog.askopenfilename()
    with open(of, 'r') as f:
        text.delete(1.0, END)
        text.insert(1.0, f.read())
        root.title(of)
    global filnamn
    filnamn = of


# Funktion för att spara det man skrivit i filen
def savefile():
    with open(filnamn, 'w') as f:
        f.write(text.get(1.0, END))


# Funktion för att spara det man skrivit i txt-fil och välja filnamn
def saveasfile():
    filename = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if filename is None:
        return

    filename.write(text.get(1.0, END))
    filename.close()


# Funktion för att kopiera det som finns i textrutan och tar bort new line i slutet
def copy():
    mark = text.get(1.0, 'end-1c')
    text.clipboard_clear()
    text.clipboard_append(mark)


# Funktion för att kunna välja font i checkbutton
def Hfont():
    global Hvar
    if Hvar.get() == 1:
        text.config(font='Helvetica')
        Tvar.set(0)
    elif Hvar.get() == 0:
        Tvar.set(0)
        text.config(font='consolas')


# Funktion för att kunna välja font i checkbutton
def Tfont():
    global Tvar
    if Tvar.get() == 1:
        text.config(font='Times')
        Hvar.set(0)
    elif Tvar.get() == 0:
        Hvar.set(0)
        text.config(font='consolas')


def writingorelse():
    while True:
        writing = text.get(1.0, END)
        time.sleep(1)
        writing2 = text.get(1.0, END)
        if writing != writing2:
            status.config(text='Writing...')
        else:
            status.config(text='Waiting...')


def deltext(event):
    global count
    if count == 0:
        text.delete(1.0, END)
        count += 1
    else:
        pass


# Variabler för fontval
Hvar = IntVar()
Tvar = IntVar()

# Title på root fönster
root.title('Emils text editor')

# Skapar en menubar med dropdown menyer
menubar = Menu(root, bg='grey')
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New', command=newfile)
filemenu.add_command(label='Open', command=fileopen)
filemenu.add_command(label='Save', command=savefile)
filemenu.add_command(label='Save as...', command=saveasfile)

filemenu.add_separator()

filemenu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Undo', command=donothing)

editmenu.add_separator()

editmenu.add_command(label='Cut', command=donothing)
editmenu.add_command(label='Copy', command=copy)
editmenu.add_command(label='Paste', command=donothing)


menubar.add_cascade(label='Edit', menu=editmenu)
status = Label(root, text='Waiting...', bd=1, relief=RAISED, anchor=W, bg='grey')
status.pack(side=BOTTOM, fill=X)

text = Text(root, bg='antique white', height=400, font='consolas')
text.insert(INSERT, 'Get to writing!')
text.pack(fill=X)

# Checkbuttons för fontval
tnrb = Checkbutton(status, text='Times', variable=Tvar, onvalue=1, offvalue=0, command=Tfont, bg='grey')

helvb = Checkbutton(status, text='Helvetica', variable=Hvar, onvalue=1, offvalue=0, command=Hfont, bg='grey')


tnrb.pack(side=RIGHT)
helvb.pack(side=RIGHT)
root.config(menu=menubar)
hej = Thread(target=writingorelse, daemon=True)
hej.start()
text.bind('<Button-1>', deltext)

root.mainloop()

