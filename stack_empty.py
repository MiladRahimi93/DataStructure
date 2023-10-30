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
# process

def stack_is_empty():
    stack = creating_stack.stack_return()
    if stack == []:
        print(style.RED + "Your stack is empty")
        input("Enter any key to close: ")
        stack_empty()
    else:
        print(style.RED + "Your stack is full.")
        input("Enter any key to close: ")
        stack_empty()
# code review
def stack_empty_review():

    print(style.WHITE + """
    # process    
    stack = creating_stack.stack_creation()
    def stack_is_empty():
    if stack == []:
        print("Your stack is empty")
        stack_empty()
    else:
        print("Your stack is full.")
        stack_empty()
    """)
    back_selection = input(style.RED +"""Enter any key to close: """)
    if back_selection == '0':
        stack_empty()
    else:
        stack_empty()




def stack_empty():
    print(style.YELLOW + """
    [+] Select an option if you didn't create stack before the process will return that stack is empty
        otherwise it will return that stack is full.
            1: stack is_empty check
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        stack_is_empty()
    elif selection == '2':
        stack_empty_review()
    elif selection == '3':
        stack_implementation.stack_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        stack_empty()

