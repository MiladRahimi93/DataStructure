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
stack = creating_stack.stack_return()
# process
def stack_size_implement():
    if stack == []:
        print(style.RED + "Your stack size is 0 it mean it doesn't contain any element.")
        input("Enter any key to close: ")
        stack_size()
    else:
        stack_size_imp = len(stack)
        print(style.RED + "The size of your stack is " + str(stack_size_imp) + " .")
        input("Enter any key to close")
        stack_size()

# review
def stack_size_review():
    print(style.WHITE +"""
    # process
def stack_size_implement():
    if stack == []:
        print(style.RED + "Your stack size is 0 it mean it doesn't contain any element.")
        input("Enter any key to close: ")
    else:
        stack_size_imp = len(stack)
        print(style.RED + "The size of your stack is " + str(stack_size_imp) + " .")
        input("Enter any key to close")
        stack_size()
    
    """)
    input(style.RED + "Enter any key to close: ")
    stack_size()


def stack_size():
    print(style.YELLOW + """
    [+] Check the size of your created stack:
            1: Created stack size
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        stack_size_implement()
    elif selection == '2':
        stack_size_review()
    elif selection == '3':
        stack_implementation.stack_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        stack_size()

