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
# start of process
stack = []
def stack_creation():
    try:
        stack_size = eval(input(style.YELLOW + "Enter the size of your stack: "))
        for i in range(stack_size):
            stack_element = input("Enter the " + str(i) + " element of your stack: ")
            stack.append(stack_element)
        print("your created stack is " + str(stack) + " .")
        back_selection = input("Enter any key to close: ")
        if back_selection == '0':
            stack_implementation.stack_implementaion()
        else:
            stack_implementation.stack_implementaion()
    except:
            print(style.RED + "[+] Invalid input try to insert an int")
            stack_creation()
returning_stack = stack
def stack_return():
    return stack
# Stack code review
def stack_code_review():
    print(style.WHITE + """
    def stack_creation():
    stack = []
    try:
        stack_size = eval(input(style.YELLOW + "Enter the size of your stack: "))
        for i in range(stack_size):
            stack_element = input("Enter the " + str(i) + " element of your stack: ")
            stack.append(stack_element)
        print("your created stack is " + str(stack) + " .")
        back_selection = input("Enter any key to close: ")
        if back_selection == '0':
            stack_implementation.stack_implementaion()
        else:
            stack_implementation.stack_implementaion()
        return stack
    except:
            print(style.RED + "[+] Invalid input try to insert an int")
            stack_creation()
    """)
    back_selection = input(style.RED +"""Enter any key to close: """)
    if back_selection == '0':
        stack_creating()
    else:
        stack_creating()



def stack_creating():
    print(style.YELLOW + """
    [+] Select an option
        1: stack creating
        2: code review
        3: back""")
    selection = input("Enter your selection: ")
    if selection == '1':
        stack_creation()
    elif selection == '2':
        stack_code_review()
    elif selection == '3':
        stack_implementation.stack_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        stack_creating()
