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

stack = creating_stack.stack_return()
def stack_pop_process():

    if stack == []:
        print(style.RED + "Your stack is Empty!")
        stack_pop()
    else:
        print(style.YELLOW + "Your stack before poping is " + str(stack) + " .")
        print("your stack after poping is " + str(stack[:-1]) + " .")
        select = input(style.RED + "Enter 0 for trying again or other key to close: ")
        if select == '0':
            stack_pop_process()
        else:
            stack_pop()
# code review
def stack_pop_review():

    print(style.WHITE + """
    # process

def stack_pop_process():
    stack = creating_stack.stack_return()
    if stack == []:
        print(style.RED + "Your stack is Empty!")
        stack_pop()
    else:
        print(style.YELLOW + "Your stack before poping is " + str(stack) + " .")
        stack = stack[:len(stack-1)]
        print("your stack after poping is " + str(stack) + " .")
        select = input(style.RED + "Enter 0 for trying again or other key to close: ")
        if select == '0':
            stack_pop_process()
        else:
            stack_pop()
    """)
    back_selection = input(style.RED +"""Enter any key to close: """)
    stack_pop()




def stack_pop():
    print(style.YELLOW + """
    [+] In pop process you will remove element at the top of your stack (LIFO).
            1: poping in stack check
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        stack_pop_process()
    elif selection == '2':
        stack_pop_review()
    elif selection == '3':
        stack_implementation.stack_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        stack_pop()

