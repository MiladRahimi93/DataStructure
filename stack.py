import cv2
import linear_dsa
import os
import stack_implementation
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
# stack definiation
def defenation_of_stack():
    print(style.YELLOW + """
    [+] A stack is a linear data structure in which the insertion of a new element and removal of an existing
        element takes place at the same end represented as the top of the stack.
        This strategy states that the element that is inserted last will come out first. You can take a pile of
        plates kept on top of each other as a real-life example. The plate which we put last is on the top and 
        since we remove the plate that is at the top, we can say that the plate that was put last comes out first.
        Basic Operations on Stack
            [+] In order to make manipulations in a stack, there are certain operations provided to us.
                1: push() to insert an element into the stack
                2: pop() to remove an element from the stack
                3: top() Returns the top element of the stack.
                4: isEmpty() returns true if stack is empty else false.
                5: size() returns the size of stack.
            [+] Types of Stacks:
                1: Fixed Size Stack: As the name suggests, a fixed size stack has a fixed size and cannot grow or shrink
                dynamically. If the stack is full and an attempt is made to add an element to it, an overflow error
                occurs. If the stack is empty and an attempt is made to remove an element from it, an underflow error
                occurs.
                2: Dynamic Size Stack: A dynamic size stack can grow or shrink dynamically. When the stack is full, it 
                automatically increases its size to accommodate the new element, and when the stack is empty, it
                decreases its size. This type of stack is implemented using a linked list, as it allows for easy 
                resizing of the stack.
                    """)
    back_select = input(style.RED + "Enter any key to close: ")
    if back_select == '0':
        test()
    else:
        test()


# main Program
def test():
    print(style.GREEN + """

    [+] Select an Option:
        1: Stack Defination
        2: stack implementation
        3: stack image
        4: Back
    """)
    stack_selection = input(style.MAGENTA + "Enter you Selection:")
    if stack_selection == '1':
        defenation_of_stack()
    elif stack_selection == '2':
        stack_implementation.stack_implementaion()
    elif stack_selection == '3':
        img = cv2.imread('stack.jpeg', cv2.IMREAD_GRAYSCALE)

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        test()
    elif stack_selection == '4':
        linear_dsa.lineardsa_implementaion()
    else:
        test()
