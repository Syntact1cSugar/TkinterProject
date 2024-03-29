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
            if (slow.data != fast.data):
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


# Driver Code : main()
d = DoublyLinkedList()
