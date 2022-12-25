import sys
import os
from tkinter import *

window = Tk()

window.title("Run Python Script")
window.geometry('550x200')


def run():
    os.system('list.py')
    return


def createNewWindow():
    newWindow = Toplevel(window)
    newWindow.title("About")
    newWindow.geometry('550x200')
    text = Text(newWindow, width=50, height=30, background="white", foreground="black", font=('Times New Roman', 13, 'bold'))
    text.insert(INSERT, "This code was contributed by : \n\n1.Subramanya H(20GACSE069) \n\n2.Suchit Priyadarshi(20GACSE070 \n\n3.Sujatha Bhat(20GACSE071)")
    text.pack(expand=1, fill=BOTH)
    btn = Button(newWindow, text="Back", bg="black", fg="white", command=newWindow.destroy)
    btn.place(x=100, y=150)
    return


btn1 = Button(window, text="Click To Run Doubly Linked List", bg="black", fg="white", command=run)
btn2 = Button(window, text="About", fg="white", bg="black", command=createNewWindow)
btn3 = Button(window, text="Exit", bg="black", fg="white", command=window.destroy)
btn1.place(x=175, y=50)
btn2.place(x=240, y=100)
btn3.place(x=245, y=150)
window.mainloop()
