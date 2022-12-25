import sys
import os
from tkinter import *


window = Tk()

window.title("Run Python Script")
window.geometry('550x200')


def run():
    os.system('list.py')


btn = Button(window, text="Click To Run Doubly Linked List", bg="black", fg="white", command=run)
btn.place(x=175, y=100)

window.mainloop()
