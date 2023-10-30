import cv2
import linked_list_implementaion
import linear_dsa
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

def link_list_print():
    print(style.WHITE + """    
    def linked_list_creating():
        class Node:
            def __init__(self, value):
                self.value = value
                self.next = None

        class LinkedList:
            def __init__(self):
                self.head = None

            def append(self, value):
                new_node = Node(value)
                if self.head is None:
                    self.head = new_node
                else:
                    current_node = self.head
                    while current_node.next:
                        current_node = current_node.next
                    current_node.next = new_node

            def display(self):
                current_node = self.head
                while current_node:
                    print(current_node.value, end=" ")
                    current_node = current_node.next
                print()
        mylist = LinkedList()

        """)
    input(style.RED + "Enter any key to close: ")
    linked_list_creation()

# implement
def linked_list_creating():
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
            else:
                current_node = self.head
                while current_node.next:
                    current_node = current_node.next
                current_node.next = new_node

        def display(self):
            current_node = self.head
            while current_node:
                print(style.YELLOW + current_node.value, end=" ")
                current_node = current_node.next
            print()

    mylist = LinkedList()
    flag = True
    element_index = 0
    while flag:
        element = input("Enter the " + str(element_index) + " element of your list or enter to close: " )
        element_index += 1
        mylist.append(element)
        if element == '':
            flag = False
    print("Your created linklist is as bellow.")
    mylist.display()
    input(style.RED + "Enter any key to close: ")
    linked_list_creation()

# review
def linked_list_creation():
    print(style.YELLOW +"""
    [+] Select an option:
        1: code review
        2: code implementaion
        3: Back
    """)
    selection = input("Enter your choice: ")
    if selection == '1':
        link_list_print()
    elif selection == '2':
        linked_list_creating()
    elif selection == '3':
        test()
    else:
        print(style.RED + "invalid input!")
        linked_list_creation()




# definiation
def linked_list_definiation():
    print(style.YELLOW + """
    [+] A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
        The elements in a linked list are linked using pointers.
        
        [+] Types of Linked List    
            1: Singly Linked List
            2: Doubly Linked List
            3: Circular Linked List
            4: Circular Doubly Linked List
            5: Header Linked List
            
        [+] Basic Operations:
            1: Linked List Insertion
            2: Search an element in a Linked List (Iterative and Recursive)
            3: Find Length of a Linked List (Iterative and Recursive)
            4: Reverse a linked list
            5: Linked List Deletion (Deleting a given key)
            6: Write a function to get Nth node in a Linked List
            7: Nth node from the end of a Linked List
        """)
    input(style.RED + "Enter any key to close: ")
    test()


# main Program
def test():
    print(style.GREEN + """

    [+] Select an Option:
        1: Linked list Defination and Types
        2: Link List creation
        3: Link List implementation
        4: Link list image
        5: Back
    """)
    array_selection = input(style.MAGENTA + "Enter you Selection:")
    if array_selection == '1':
        linked_list_definiation()
    elif array_selection == '2':
        linked_list_creation()
    elif array_selection == '3':
        linked_list_implementaion.implement()
    elif array_selection == '4':
        img = cv2.imread('linked.png', cv2.IMREAD_GRAYSCALE)

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        test()
    elif array_selection == '5':
        linear_dsa.lineardsa_implementaion()
    else:
        test()
