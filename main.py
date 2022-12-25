import sys
import os
from tkinter import *

window = Tk()

window.title("Run Python Script")
window.geometry('550x200')


def run():
    os.system('list.py')
    return


def createNewWindow1():
    newWindow = Toplevel(window)
    newWindow.title("List of APIs")
    newWindow.geometry('550x200')
    text = Text(newWindow, width=50, height=30, background="white", foreground="black",font=('Times New Roman', 13, 'bold'))
    text.insert(INSERT,"Doubly Linked List API : \n\n1.Insert Node(Front and Rear) \n\n2.Delete Node(Front and Rear) "
                       "\n\n3.Reverse List \n\n4.Sort List \n\n 5.Remove Duplicates")
    text.pack(expand=1, fill=BOTH)
    btn = Button(newWindow, text="Back", bg="black", fg="white", command=newWindow.destroy)
    btn.place(x=500, y=0)
    return


def createNewWindow2():
    newWindow = Toplevel(window)
    newWindow.title("About")
    newWindow.geometry('550x200')
    text = Text(newWindow, width=50, height=30, background="white", foreground="black",
                font=('Times New Roman', 13, 'bold'))
    text.insert(INSERT,"This code was contributed by : \n\n1.Subramanya H(20GACSE069) \n\n2.Suchit Priyadarshi("
                       "20GACSE070) \n\n3.Sujatha Bhat(20GACSE071)")
    text.pack(expand=1, fill=BOTH)
    btn = Button(newWindow, text="Back", bg="black", fg="white", command=newWindow.destroy)
    btn.place(x=500, y=0)
    return


# Four buttons on parent window
btn1 = Button(window, text="Run Doubly Linked List", bg="black", fg="white", command=run)
btn2 = Button(window, text="List of Operations Implemented", fg="white", bg="black", command=createNewWindow1)
btn3 = Button(window, text="About", fg="white", bg="black", command=createNewWindow2)
btn4 = Button(window, text="Exit", bg="black", fg="white", command=window.destroy)

# Positions of each button
btn1.place(x=200, y=0)
btn2.place(x=175, y=50)
btn3.place(x=240, y=100)
btn4.place(x=245, y=150)

window.mainloop()
