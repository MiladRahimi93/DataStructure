import os
import stack_implementation
import creating_stack
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
def stack_top_check():
    stack = creating_stack.stack_return()
    if stack == []:
        print(style.RED + "Your stack is empty")
        input("Enter any key to close: ")
        stack_top()
    else:
        print(style.RED + "Your stack top element is " + str(stack[-1]) +" .")
        input("Enter any key to close: ")
        stack_top()

def stack_top_review():
    print(style.WHITE + """
    def stack_top_check():
    stack = creating_stack.stack_return()
    if stack == []:
        print(style.RED + "Your stack is empty")
        input("Enter any key to close: ")
        stack_top()
    else:
        print(style.RED + "Your stack top element is " + str(stack[-1]) +" .")
        input("Enter any key to close: ")
        stack_top()
    
    
    """)
    input(style.RED + "Enter any key to close: ")
    stack_top()

def stack_top():
    print(style.YELLOW + """
    [+] The "top" element of the stack is the element that was last pushed and will be the first to be popped.
        The "bottom" element of the stack is the one that, when removed, will leave the stack empty.
            1: Check the top element in your created stack
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        stack_top_check()
    elif selection == '2':
        stack_top_review()
    elif selection == '3':
        stack_implementation.stack_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        stack_top()

