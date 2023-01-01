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
        newNode = Node(data, None, self.__head)
        if self.__head is not None:
            self.__head.prev = newNode
        self.__head = newNode
        return True  # insert success

    def insertRear(self, data):
        curr = self.__head
        if curr is None:  # List is empty
            self.__head = Node(data, None, None)
        else:
            # take curr to the last node
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data, curr, None)
        return True  # insert success

    # Delete operations on the linked list :

    def deleteFront(self):
        if self.__head is None:  # List is empty
            return False  # delete failure
        # Shift the header to the leading node
        self.__head = self.__head.next
        if self.__head is not None:
            self.__head.prev = None
        return True  # delete success

    def deleteRear(self):
        if self.__head is None:  # List is empty
            return False  # delete failure
        prev, curr = self.__head, self.__head
        # take curr to the last node and prev to the penultimate node
        while curr.next is not None:
            prev = curr
            curr = curr.next
        if curr == self.__head:  # last node is the header node itself
            self.__head = None
        else:
            prev.next = None
        del curr
        return True  # delete success

    def deleteAll(self):
        if self.__head is None:
            return False

        curr = self.__head
        while curr is not None:
            delNode = curr
            curr = delNode.next
            del delNode

        self.__head = None
        return True

    # Utility operations on the linked list :
    def printList(self):
        curr = self.__head
        entries = []
        # curr pointer traverses the linked list from header to the last node
        while curr is not None:
            entries.append(str(curr.data))
            curr = curr.next
        return entries

    def reverse(self):
        if self.__head is None:
            return False
        curr = self.__head
        while curr is not None:
            curr.prev, curr.next = curr.next, curr.prev
            self.__head = curr
            curr = curr.prev
        return True

    # Insertion Sort (Non Decreasing Order)
    def sort(self):
        curr = self.__head
        if curr is None:
            return True
        while curr is not None:
            value, back = curr.data, curr
            while back.prev is not None and back.prev.data > value:
                back.data = back.prev.data
                back = back.prev
            back.data = value
            curr = curr.next

    def removeDuplicates(self):
        curr = self.__head
        if curr is None:
            return False
        # two pointer appraoch by sorting
        self.sort()
        slow, fast = curr, curr.next
        # slow + 1st node marks the end of unique numbers

        while fast is not None:
            if slow.data != fast.data:
                slow = slow.next
                slow.data = fast.data
            fast = fast.next

        # slow + 1th node till end are redundant nodes therefore delete those
        curr = slow.next
        slow.next = None

        while curr is not None:
            delNode = curr
            curr = delNode.next
            del delNode

        return True


# End of Doubly Linked List Implementation


# Utility Functions for button hovering effects
def on_enter_gray(e):
    e.widget['background'] = '#363636'


def on_leave_black(e):
    e.widget['background'] = 'black'


# Events that will be invoked upon clicking the buttons
def insert_front_event(data, updated_button):
    dll.insertFront(data)
    updated_button.flash()


def insert_rear_event(data, updated_button):
    dll.insertRear(data)
    updated_button.flash()


def delete_front_event(updated_button):
    dll.deleteFront()
    updated_button.flash()


def delete_rear_event(updated_button):
    dll.deleteRear()
    updated_button.flash()


def delete_all_event(updated_button):
    dll.deleteAll()
    updated_button.flash()


def reverse_event(updated_button):
    dll.reverse()
    updated_button.flash()


def sort_event(updated_button):
    dll.sort()
    updated_button.flash()


def remove_duplicates_event(updated_button):
    dll.removeDuplicates()
    updated_button.flash()


def print_event(outputText, updated_button):
    outputText.delete("1.0", "end")
    for s in dll.printList():
        outputText.insert(END, s)
        outputText.insert(END, "\t")
    updated_button.flash()
    return


# End of event functions


def run():
    # Create the main window
    newWindow = Toplevel(window)
    newWindow.title("Doubly Linked List")
    newWindow.geometry("1000x1000")
    newWindow.configure(bg='#d6d6d6')

    # StringVar() variable for the text variable option in entry()
    inputValue = tkinter.StringVar()

    # Output label
    tkinter.Label(newWindow, font=('Comic Sans MS', 15, 'bold'), text="Input").pack(pady=(5, 5))

    # create a text entry to take input
    inputEntry = tkinter.Entry(newWindow, font=('Comic Sans MS', 15, 'bold'), width=20, justify=CENTER,
                               textvariable=inputValue)
    inputEntry.pack(pady=(5, 5))

    # A button that blinks upon completion of an operation
    updated_button = tkinter.Button(newWindow, font=('Comic Sans MS', 10, 'bold'), text="✓", height=1, width=5)
    updated_button['activebackground'] = 'green'
    updated_button['background'] = 'black'
    updated_button['foreground'] = 'white'
    updated_button.pack(pady=(5, 5))
    # Create a button to insert front of the list
    insert_front_button = tkinter.Button(newWindow, font=buttonFont, text="Insert Front 𝒪(𝐼)",
                                         command=lambda: insert_front_event(int(inputValue.get()), updated_button)
                                         if inputValue.get().isnumeric() else None)
    insert_front_button['background'] = "black"
    insert_front_button['foreground'] = 'white'
    insert_front_button.bind("<Enter>", on_enter_gray)
    insert_front_button.bind("<Leave>", on_leave_black)
    insert_front_button.pack(pady=(5, 5))

    # Create a button to insert rear of the list
    insert_rear_button = tkinter.Button(newWindow, font=buttonFont, text="Insert Rear 𝒪(𝑛)",
                                        command=lambda: insert_rear_event(int(inputValue.get()), updated_button)
                                        if inputValue.get().isnumeric() else None)
    insert_rear_button['background'] = 'black'
    insert_rear_button['foreground'] = 'white'
    insert_rear_button.bind("<Enter>", on_enter_gray)
    insert_rear_button.bind("<Leave>", on_leave_black)
    insert_rear_button.pack(pady=(5, 5))

    # Create a button to delete the node at the front of the list
    delete_front_button = tkinter.Button(newWindow, font=buttonFont, text="Delete Front 𝒪(𝐼)",
                                         command=lambda: delete_front_event(updated_button))
    delete_front_button['background'] = 'black'
    delete_front_button['foreground'] = 'white'
    delete_front_button.bind("<Enter>", on_enter_gray)
    delete_front_button.bind("<Leave>", on_leave_black)
    delete_front_button.pack(pady=(5, 5))

    # Create a button to delete the node at the end of the list
    delete_rear_button = tkinter.Button(newWindow, font=buttonFont, text="Delete Rear 𝒪(𝑛)",
                                        command=lambda: delete_rear_event(updated_button))
    delete_rear_button['foreground'] = 'white'
    delete_rear_button['background'] = 'black'
    delete_rear_button.bind("<Enter>", on_enter_gray)
    delete_rear_button.bind("<Leave>", on_leave_black)
    delete_rear_button.pack(pady=(5, 5))

    # Create a button to delete all nodes in the linked list
    delete_all_button = tkinter.Button(newWindow, font=buttonFont, text="Delete All 𝒪(𝑛)",
                                       command=lambda: delete_all_event(updated_button))
    delete_all_button['background'] = 'black'
    delete_all_button['foreground'] = 'white'
    delete_all_button.bind("<Enter>", on_enter_gray)
    delete_all_button.bind("<Leave>", on_leave_black)
    delete_all_button.pack(pady=(5, 5))

    # Create a button to reverse the list
    reverse_button = tkinter.Button(newWindow, font=buttonFont, text="Reverse 𝒪(𝑛)",
                                    command=lambda: reverse_event(updated_button))
    reverse_button['background'] = 'black'
    reverse_button['foreground'] = 'white'
    reverse_button.bind("<Enter>", on_enter_gray)
    reverse_button.bind("<Leave>", on_leave_black)
    reverse_button.pack(pady=(5, 5))

    # Create a button to sort the list
    sort_button = Button(newWindow, font=buttonFont, text="Sort 𝒪(𝑛^2)",
                         command=lambda: sort_event(updated_button))
    sort_button['background'] = 'black'
    sort_button['foreground'] = 'white'
    sort_button.bind("<Enter>", on_enter_gray)
    sort_button.bind("<Leave>", on_leave_black)
    sort_button.pack(pady=(5, 5))

    # Create a button to remove duplicates from the list
    remove_duplicates_button = tkinter.Button(newWindow, font=buttonFont, text="Remove Duplicates 𝒪(𝑛^2)",
                                              command=lambda: remove_duplicates_event(updated_button))
    remove_duplicates_button['background'] = 'black'
    remove_duplicates_button['foreground'] = 'white'
    remove_duplicates_button.bind("<Enter>", on_enter_gray)
    remove_duplicates_button.bind("<Leave>", on_leave_black)
    remove_duplicates_button.pack(pady=(5, 5))

    # Create a button to print / traverse the list

    print_list_button = tkinter.Button(newWindow, font=buttonFont, text='Traverse 𝒪(𝑛)',
                                       command=lambda: print_event(outputText, updated_button))
    print_list_button['background'] = 'black'
    print_list_button['foreground'] = 'white'
    print_list_button.bind("<Enter>", on_enter_gray)
    print_list_button.bind("<Leave>", on_leave_black)
    print_list_button.pack(pady=(5, 5))

    # Output Label
    tkinter.Label(newWindow, font=('Comic Sans MS', 15, 'bold'), text="Output : ").pack(pady=(5, 5))

    # Text widget for displaying output
    outputText = tkinter.Text(newWindow, font=("Comic Sans MS", 15, 'bold'), width=80, height=3)
    outputText.tag_configure("tag_name", justify="center")
    outputText.pack()

    # Back Button
    back_btn = Button(newWindow, font=buttonFont, width=5, height=1, text="◁", bg="black", fg="white",
                      command=newWindow.destroy)
    back_btn.pack(pady=(10, 10), fill=X)
    # Hovering for the back btn
    back_btn.bind("<Enter>", on_enter_gray)
    back_btn.bind("<Leave>", on_leave_black)


def api_info():
    newWindow = Toplevel(window)
    newWindow.title("List of APIs")
    newWindow.geometry('1000x1000')
    newWindow.configure(bg='#d6d6d6')
    text1 = Text(newWindow, width=50, height=20, background="white", foreground="black",
                 font=('Comic Sans MS', 20, 'bold'))
    text1.pack(anchor='center')
    text1.insert(END, "Operations on the doubly linked list :")
    text1.insert(END, "\n\n1.Insert Node")
    text1.insert(END, "\n->Insert Front: This function adds a new node at the beginning of the linked list.")
    text1.insert(END, "\nTime complexity: 𝒪(𝐼)\tSpace complexity: 𝒪(𝐼)")
    text1.insert(END, "\n\n->Insert Rear: This function adds a new node at the end of the linked list.")
    text1.insert(END, "\nTime complexity: 𝒪(𝑛)\tSpace complexity: 𝒪(𝐼)")
    text1.insert(END, "\n\n2.Delete Node")
    text1.insert(END, "\n->Delete Front: This function deletes a node at the beginning of the linked list.")
    text1.insert(END, "\nTime complexity: 𝒪(𝐼)\tSpace complexity: 𝒪(𝐼)")
    text1.insert(END, "\n\n->Delete Rear: This function deletes a node at the end of the linked list.")
    text1.insert(END, "\nTime complexity: 𝒪(𝑛)\tSpace complexity: 𝒪(𝐼)")
    text1.insert(END, "\n\n->Delete All: This function deletes all the nodes in the linked list.")
    text1.insert(END, "\nTime complexity: 𝒪(𝑛)\tSpace complexity: 𝒪(𝐼)")
    text1.insert(END, "\n\n3.Reverse List: This function iteratively reverses the linked list by swapping the values "
                      "of previous and next pointers also updating the header node pointer.")
    text1.insert(END, "\nTime complexity: 𝒪(𝑛)\tSpace complexity: 𝒪(𝐼)")
    text1.insert(END, "\n\n4.Sort List: This function uses insertion sort technique to sort the list.The sorting is "
                      "in-place, stable and quadratic in time.")
    text1.insert(END, "\nTime complexity: 𝒪(𝑛^2)\tSpace complexity: 𝒪(𝐼)")
    text1.insert(END, "\n\n5.Remove Duplicates: This function makes use of sort() function and two pointer technique "
                      "to remove duplicate entries.")
    text1.insert(END, "\nTime complexity: 𝒪(𝑛^2)\tSpace complexity: 𝒪(𝐼)")

    # Back Button
    back_btn = Button(newWindow, font=buttonFont, width=5, height=1, text="◁", bg="black", fg="white",
                      command=newWindow.destroy)
    back_btn.pack(fill=X)
    # Hovering for the back btn
    back_btn.bind("<Enter>", on_enter_gray)
    back_btn.bind("<Leave>", on_leave_black)
    return


def about():
    newWindow = Toplevel(window)
    newWindow.title("About")
    newWindow.geometry('1000x1000')
    newWindow.configure(bg='#d6d6d6')

    text = Text(newWindow, width=50, height=20, background="white", foreground="black",
                font=('Comic Sans MS', 20, 'bold'))
    text.pack(anchor='center')
    text.insert(INSERT, "This code was contributed by : \n\n1.Subramanya H (20GACSE069) \n\n2.Suchit Priyadarshi ("
                        "20GACSE070) \n\n3.Sujatha Bhat (20GACSE071)")

    # Back Button
    back_btn = Button(newWindow, font=buttonFont, width=5, height=1, text="◁", bg="black", fg="white",
                      command=newWindow.destroy)
    back_btn.pack(fill=X)
    # Hovering for the back btn
    back_btn.bind("<Enter>", on_enter_gray)
    back_btn.bind("<Leave>", on_leave_black)
    return


# Main Menu
dll = DoublyLinkedList()

window = Tk()
window.title("Root Window")
window.geometry('1000x1000')
window.configure(bg='#d6d6d6')

# Universal font for buttons
buttonFont = font.Font(family='Comic Sans MS', size=15, weight='bold')

# Four buttons on parent window

run_btn = Button(window, height=7, width=70, font=buttonFont, text="▷ Run Doubly Linked List", bg="black",
                 fg="white", command=run)
list_btn = Button(window, height=7, width=70, font=buttonFont, text="⏍ List of Operations", justify=CENTER,
                  fg="white", bg="black", command=api_info)
about_btn = Button(window, height=7, width=70, font=buttonFont, text="⌕ About", justify=CENTER, fg="white", bg="black",
                   command=about)
exit_btn = Button(window, height=7, width=70, font=buttonFont, text="⨷ Exit", justify=CENTER, bg="black", fg="white",
                  command=window.destroy)

# Positions of each button
run_btn.pack(anchor='center', pady=(5, 5))
list_btn.pack(anchor='center', pady=(5, 5))
about_btn.pack(anchor='center', pady=(5, 5))
exit_btn.pack(anchor='center', pady=(5, 5))

# Hovering effects for button
run_btn.bind("<Enter>", on_enter_gray)
run_btn.bind("<Leave>", on_leave_black)
list_btn.bind("<Enter>", on_enter_gray)
list_btn.bind("<Leave>", on_leave_black)
about_btn.bind("<Enter>", on_enter_gray)
about_btn.bind("<Leave>", on_leave_black)
exit_btn.bind("<Enter>", on_enter_gray)
exit_btn.bind("<Leave>", on_leave_black)

window.mainloop()

del dll
