import sys
import os
import tkinter
from tkinter import *
import tkinter.font as font

# Doubly Linked List Implementation

class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.__head = None  # head is a private member(pointer)that points to the header node of the linked list

    # Insert operations on the linked list :
    def insertFront(self, data):
        print(data)
        newNode = Node(data, None, self.__head)
        if (self.__head != None):
            self.__head.prev = newNode
        self.__head = newNode
        return True  # insert success

    def insertRear(self, data):
        curr = self.__head
        if (curr == None):  # List is empty
            self.__head = Node(data, None, None)
        else:
            # take curr to the last node
            while (curr.next != None):
                curr = curr.next
            curr.next = Node(data, curr, None)
        return True  # insert success

    # Delete operations on the linked list :

    def deleteFront(self):
        if (self.__head == None):  # List is empty
            return False  # delete failure
        # Shift the header to the leading node
        self.__head = self.__head.next
        if (self.__head != None):
            self.__head.prev = None
        return True  # delete success

    def deleteRear(self):
        if (self.__head == None):  # List is empty
            return False  # delete failure
        prev, curr = self.__head, self.__head
        # take curr to the last node and prev to the penultimate node
        while (curr.next != None):
            prev = curr
            curr = curr.next
        if (curr == self.__head):  # last node is the header node itself
            self.__head = None
        else:
            prev.next = None
        del curr
        return True  # delete success

    # Utility operations on the linked list :
    def printList(self):
        print("List contains : ", end=' ')
        curr = self.__head;
        # curr pointer traverses the linked list from header to the last node
        while (curr != None):
            print(curr.data)
            curr = curr.next
        return True

    def reverse(self):
        if (self.__head == None): return False
        curr = self.__head
        while (curr != None):
            curr.prev, curr.next = curr.next, curr.prev
            self.__head = curr
            curr = curr.prev
        return True

    # Insertion Sort (Non Decreasing Order)
    def sort(self):
        curr = self.__head
        if (curr == None): return True
        while (curr != None):
            value, back = curr.data, curr
            while (back.prev != None and back.prev.data > value):
                back.data = back.prev.data
                back = back.prev
            back.data = value
            curr = curr.next

    def removeDuplicates(self):
        curr = self.__head
        if (curr == None): return False
        # two pointer appraoch by sorting
        self.sort()
        slow, fast = curr, curr.next
        # slow + 1th node marks the end of unique numbers

        while (fast != None):
            if slow.data != fast.data:
                slow = slow.next
                slow.data = fast.data
            fast = fast.next

        # slow + 1th node till end are redundant nodes therefore delete those
        curr = slow.next
        slow.next = None

        while (curr != None):
            delNode = curr
            curr = curr.next
            del delNode

        return True


# End of Doubly Linked List Implementation


def run():
    # Create the main window
    window1 = Toplevel(window)
    window1.title("Doubly Linked List")
    window1.geometry("1000x1000")

    tkinter.Label(window1, font=('Consolas', 15, 'underline', 'bold'), text="Input").pack()

    # StringVar() variable for the textvariable option in entry()
    input = tkinter.StringVar()
    # Create a text entry widget to enter values
    inputEntry = tkinter.Entry(window1, justify=CENTER, textvariable=input)
    inputEntry.pack(pady=(10, 10))

    # Create a button to insert a value at the front of the list
    insert_front_button = tkinter.Button(window1, font=buttonFont, text="Insert Front",
                                         command=lambda: dll.insertFront(int(input.get())))
    insert_front_button.pack(pady=(10, 10))

    # Create a button to insert a value at the end of the list
    insert_rear_button = tkinter.Button(window1, font=buttonFont, text="Insert Rear", command=lambda: dll.insertRear(int(input.get())))
    insert_rear_button.pack(pady=(10, 10))

    # Create a button to delete the node at the front of the list
    delete_front_button = tkinter.Button(window1, font=buttonFont, text="Delete Front", command=dll.deleteFront)
    delete_front_button.pack(pady=(10, 10))

    # Create a button to delete the node at the end of the list
    delete_rear_button = tkinter.Button(window1, font=buttonFont, text="Delete Rear", command=dll.deleteRear)
    delete_rear_button.pack(pady=(10, 10))

    # Create a button to reverse the list
    reverse_button = tkinter.Button(window1, font=buttonFont, text="Reverse", command=dll.reverse)
    reverse_button.pack(pady=(10, 10))

    # Create a button to sort the list
    sort_button = Button(window1, font=buttonFont, text="Sort", command=dll.sort)
    sort_button.pack(pady=(10, 10))

    # Create a button to remove duplicates from the list
    remove_duplicates_button = tkinter.Button(window1, font=buttonFont, text="Remove Duplicates", command=dll.removeDuplicates)
    remove_duplicates_button.pack(pady=(10, 10))

    back = tkinter.Button(window1, font=buttonFont, text="Remove Duplicates", command=window1.destroy)
    back.pack(pady=(10, 10))



    tkinter.Label(window1, font=('Consolas', 15, 'underline', 'bold'), text="Output").pack()
    # Output entry widget
    outputEntry = tkinter.Entry(window1, justify=CENTER, textvariable=input)
    outputEntry.pack()


def api_info():
    newWindow = Toplevel(window)
    newWindow.title("List of APIs")
    newWindow.geometry('1000x1000')
    text = Text(newWindow, width=50, height=30, background="white", foreground="black",
                font=('Consolas 15', 13, 'bold'))
    text.insert(INSERT, "Doubly Linked List API : \n\n1.Insert Node(Front and Rear) \n\n2.Delete Node(Front and Rear) "
                        "\n\n3.Reverse List \n\n4.Sort List \n\n 5.Remove Duplicates")
    text.pack(expand=1, fill=BOTH)
    btn = Button(newWindow, text="Back", bg="black", fg="white", command=newWindow.destroy)
    btn.place(x=950, y=0)
    return


def about():
    newWindow = Toplevel(window)
    newWindow.title("About")
    newWindow.geometry('1000x1000')
    text = Text(newWindow, width=50, height=30, background="white", foreground="black",
                font=('Consolas 15', 13, 'bold'))
    text.insert(INSERT, "This code was contributed by : \n\n1.Subramanya H(20GACSE069) \n\n2.Suchit Priyadarshi("
                        "20GACSE070) \n\n3.Sujatha Bhat(20GACSE071)")
    text.pack(expand=1, fill=BOTH)
    btn = Button(newWindow, text="Back", bg="black", fg="white", command=newWindow.destroy)
    btn.place(x=950, y=0)
    return


# Four buttons on parent window


# Main Menu
dll = DoublyLinkedList()

window = Tk()
window.title("Run Python Script")
window.geometry('1000x1000')
buttonFont = font.Font(family='Consolas 15', size=16, weight='bold')

# Scroll bar for this window

btn1 = Button(window, height=10, width=80, font=buttonFont, text="Run Doubly Linked List", justif=CENTER, bg="black", fg="white", command=run)
btn2 = Button(window, height=10, width=80, font=buttonFont, text="List of Operations Implemented", justify=CENTER, fg="white", bg="black", command=api_info)
btn3 = Button(window, height=10, width=80, font=buttonFont, text="About", justify=CENTER, fg="white", bg="black", command=about)
btn4 = Button(window, height=10, width=80, font=buttonFont, text="Exit", justify=CENTER, bg="black", fg="white", command=window.destroy)

# Positions of each button
btn1.grid(row=0)
btn2.grid(row=1)
btn3.grid(row=2)
btn4.grid(row=3)

window.mainloop()
dll.printList()
