from tkinter import *
from tkinter.filedialog import *

filename = None


def newFile():
    global filename
    filename = 'Untitled'
    text.delete(0.0, END)


def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()


def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)

    try:
        f.write(t.rstrip())
    except:
        showerror(title='Oops!', message='Unable to save file...')


def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
