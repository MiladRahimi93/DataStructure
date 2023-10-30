import os
import queue_implementaion
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
queue = []
def queue_creation():
    try:
        queue_size = eval(input(style.YELLOW + "Enter the size of your queue: "))
        for i in range(queue_size):
            queue_element = input("Enter the " + str(i) + " element of your queue: ")
            queue.append(queue_element)
        print("your created queue is " + str(queue) + " .")
        back_selection = input("Enter any key to close: ")
        if back_selection == '0':
            queue_implementaion.queue_implementaion()
        else:
            queue_implementaion.queue_implementaion()
    except:
            print(style.RED + "[+] Invalid input try to insert an int")
            queue_creation()
returning_queue = queue
def queue_return():
    return queue
# queue code review
def queue_code_review():
    print(style.WHITE + """
# start of process
queue = []
def queue_creation():
    try:
        queue_size = eval(input(style.YELLOW + "Enter the size of your queue: "))
        for i in range(queue_size):
            queue_element = input("Enter the " + str(i) + " element of your queue: ")
            queue.append(queue_element)
        print("your created queue is " + str(queue) + " .")
        back_selection = input("Enter any key to close: ")
        if back_selection == '0':
            queue_implementaion.queue_implementaion()
        else:
            queue_implementaion.queue_implementaion()
    except:
            print(style.RED + "[+] Invalid input try to insert an int")
            queue_creation()
returning_queue = queue
def queue_return():
    return queue    """)
    back_selection = input(style.RED +"""Enter any key to close: """)
    if back_selection == '0':
        queue_creating()
    else:
        queue_creating()



def queue_creating():
    print(style.YELLOW + """
    [+] Select an option
        1: queue creating
        2: code review
        3: back""")
    selection = input("Enter your selection: ")
    if selection == '1':
        queue_creation()
    elif selection == '2':
        queue_code_review()
    elif selection == '3':
        queue_implementation.queue_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        queue_creating()
