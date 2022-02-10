from tkinter import *

def say_hello():
    print("Hello")
mainwindow = Tk()
label = Label(mainwindow, text="Hello TKinter").pack(side=LEFT, fill=BOTH)
button = Button(mainwindow, text="Click me", command=say_hello).pack(side=LEFT, fill=BOTH)
mainwindow.mainloop()