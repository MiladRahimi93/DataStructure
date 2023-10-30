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

def stack_pushing_process():
        stack = creating_stack.stack_return()
        print(style.YELLOW + "Your stack before pushing is " + str(stack) + " .")
        pushing_element = input("Enter the element for pushing: ")
        stack.append(pushing_element)
        print("your stack after pushing is " + str(stack) + " .")
        select = input(style.RED + "Enter 0 for trying again or other key to close: ")
        if select == '0':
            stack_pushing_process()
        else:
            stack_push()
# code review
def stack_push_review():

    print(style.WHITE + """
    # process

def stack_pushing_process():
    stack = creating_stack.stack_return()
    if stack == []:
        print(style.RED + "Your stack is empty")
        input("Enter any key to close: ")
        stack_push()
    else:
        print(style.RED + "Your stack before pushing is " + str(stack) + " .")
        pushing_element = input("Enter the element for pushing: ")
        stack = stack.append(pushing_element)
        input("your stack after pushing is " + str(stack) + " .")
        select = input(style.RED + "Enter a 0 for trying again or other key to close: ")
        if select == '0':
            stack_pushing_process()
        else:
        stack_empty()

    """)
    back_selection = input(style.RED +"""Enter any key to close: """)
    if back_selection == '0':
        stack_push()
    else:
        stack_push()




def stack_push():
    print(style.YELLOW + """
    [+] In pushing process you will add element at the top of your stack (LIFO).
            1: pushing in stack check
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        stack_pushing_process()
    elif selection == '2':
        stack_push_review()
    elif selection == '3':
        stack_implementation.stack_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        stack_push()

