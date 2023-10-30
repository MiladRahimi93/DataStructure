import  linked_list
import os

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

 # start of implementaion
# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a LinkedList class


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Method to add a node at the end of LL

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list
    # at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list

    def remove_first_node(self):
        if (self.head == None):
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while (current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        while (current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next





def implement():
    print(style.YELLOW + "For implementition first create your Linked list.")
    size = 1
    flag = True
    mylist = LinkedList()
    while flag:
        element = input("Enter the " + str(size) + " node of the list or enter to close: ")
        mylist.insertAtBegin(element)
        size+=1
        if element =='':
            print("Your created list is as bellow: ")
            mylist.printLL()
            print("""
    [+] Which process you want to do: 
        1: insertion at the begining
        2: insert at the end
        3: insert at index 
        4: update node
        5: remove first node
        6: remove last node
        7: remove at index  
        8: remove by value
        9: size of list
        10: code review
        11: close 
                          """)
            selection = input(style.GREEN + "Enter your selection: ")
            if selection == '1':
                element = input("Enter the element to insert at the begining: ")
                print("Your list before insertion is as bellow")
                mylist.printLL()
                mylist.insertAtBegin(element)
                print('')
                print(style.YELLOW + "Your list after insertion is as bellow.")
                mylist.printLL()
                input("Enter any key to back: ")
                break
            elif selection == '2':
                element = input("Enter the element to insert at the end: ")
                print("Your list before insertion is as bellow")
                mylist.printLL()
                mylist.insertAtEnd(element)
                print('')
                print(style.YELLOW + "Your list after insertion is as bellow.")
                mylist.printLL()
                input("Enter any key to back: ")
                break
            elif selection == '3':
                try:
                    element = input("Enter the element to insert: ")
                    index = eval(input("Enter the index of element to insert: "))
                    print("Your list before insertion is as bellow")
                    mylist.printLL()
                    mylist.insertAtIndex(element,index+1)
                    print('')
                    print(style.YELLOW + "Your list after insertion is as bellow.")
                    mylist.printLL()
                    input("Enter any key to back: ")
                    break
                except:
                    print("Invalid index input!!")
                    break

            elif selection == '4':
                try:
                    element = input("Enter the element value to update: ")
                    index = eval(input("Enter the index of element to update: "))
                    print("Your list before updating is as bellow: ")
                    mylist.printLL()
                    mylist.updateNode(element, index+1)
                    print('')
                    print(style.YELLOW + "Your list after insertion is as bellow.")
                    mylist.printLL()
                    input("Enter any key to back: ")
                    break
                except:
                    print("Invalid index input!!")
                    break
            elif selection == '5':
                print("Your list before removing first node is as bellow")
                mylist.printLL()
                mylist.remove_at_index(1)
                print('')
                print(style.YELLOW + "Your list after removing is as bellow.")
                mylist.printLL()
                input("Enter any key to back: ")
                break
            elif selection == '6':
                print("Your list before removing last node is as bellow")
                mylist.printLL()
                mylist.remove_last_node()
                print('')
                print(style.YELLOW + "Your list after removing last node is as bellow.")
                mylist.printLL()
                input("Enter any key to back: ")
                break
            elif selection == '7':
                try:
                    index = eval(input("Enter the index of element to remove: "))
                    print("Your list before removing the node is as bellow")
                    mylist.printLL()
                    mylist.remove_at_index(index)
                    print('')
                    print(style.YELLOW + "Your list after insertion is as bellow.")
                    mylist.printLL()
                    input("Enter any key to back: ")
                    break
                except:
                    print("Invalid index input!!")
                    break
            elif selection == '8':
                try:
                    element = input("Enter the element to remove: ")
                    print("Your list before insertion is as bellow")
                    mylist.printLL()
                    mylist.remove_node(element)
                    print('')
                    print(style.YELLOW + "Your list after insertion is as bellow.")
                    mylist.printLL()
                    input("Enter any key to back: ")
                    break
                except:
                    print("Invalid node entered!")
                    break
            elif selection == '9':
                    print("The size of linked list is " + str(mylist.sizeOfLL()) + " .")
                    break
            elif selection == '10':
                    print(style.WHITE + """
 # start of implementaion
# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a LinkedList class


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Method to add a node at the end of LL

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list
    # at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list

    def remove_first_node(self):
        if (self.head == None):
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while (current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        while (current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next

                    """)
                    input("Enter any key to close: ")
                    pass
            else:
                print(style.RED + "Invalid selection!")
                linked_list.test()
    linked_list.test()