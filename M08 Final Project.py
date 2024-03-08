# Author:  Jenna Helm
# Date written: 03/08/2024
# Assignment: This creates a tkinter application that gives a simple calculator that can be used only by students.

from tkinter import *
from tkinter import messagebox

# Code in order to run an addition soltion
def add():
    result = float(e1.get()) + float(e2.get())
    result = round(result, 4)
    label_text.set(result)
# Code in order to run an subtraction soltion
def subtract():
    result = float(e1.get()) - float(e2.get())
    result = round(result, 4)
    label_text.set(result)
# Code in order to run an muiltiplication soltion
def multiply():
    result = float(e1.get()) * float(e2.get())
    result = round(result, 4)
    label_text.set(result)
# Code in order to run an division soltion
def divide():
    result = float(e1.get()) / float(e2.get())
    result = round(result, 4)
    label_text.set(result)
def exitCode():
    exit() 
#GUI part completed

#What the application will look like...
window = Tk()
label_text = StringVar()
#Found how to add "grid" in tkinter through a video so I am using what I have learned

#title and labels
Label(window, text="Enter first Number:").grid(row=0, column=0, sticky=W)
Label(window, text="Enter second Number:").grid(row=1, column=0, sticky=W)
Label(window, text="Result:").grid(row=3, column=0, sticky=W)
Label(window, text="", textvariable=label_text).grid(row=3, column=1, sticky=W)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Buttons should actually work, found I need five altogether, follows grid
button1 = Button(window, text="Add", width=10, command=add)
button1.config(font=("Times New Roman", 12))
button1.grid(row=0, column=2, padx=5, pady=5, sticky=W)

button2 = Button(window, text="Subtract", width=10, command=subtract)
button2.config(font=("Times New Roman", 12))
button2.grid(row=0, column=3, padx=5, pady=5, sticky=W)

button3 = Button(window, text="Multiply", width=10, command=multiply)
button3.config(font=("Times New Roman", 12))
button3.grid(row=1, column=2, padx=5, pady=5, sticky=W)

button4 = Button(window, text="Divide", width=10, command=divide)
button4.config(font=("Times New Roman", 12))
button4.grid(row=1, column=3, padx=5, pady=5, sticky=W)

button5 = Button(window, text="Quit", width=10, command=exitCode, bg="red")
button5.config(font=("Times New Roman", 12))
button5.grid(row=2, column=2, padx=5, pady=5, sticky=W)

def exitCode():
    messagebox.showinfo('Thank you, goodbye')

#Will run with this
window.mainloop()