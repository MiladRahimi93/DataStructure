import os
import queue_implementaion
import queue_creating


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


def queue_rear_check():
    queue = queue_creating.queue_return()
    if queue == []:
        print(style.RED + "Your queue is empty")
        input("Enter any key to close: ")
        queue_rear()
    else:
        print(style.RED + "Your queue rear element is " + str(queue[-1]) + " .")
        input("Enter any key to close: ")
        queue_rear()


def queue_rear_review():
    print(style.WHITE + """
    def queue_rear_check():
    queue = queue_creating.queue_return()
    if queue == []:
        print(style.RED + "Your queue is empty")
        input("Enter any key to close: ")
        queue_rear()
    else:
        print(style.RED + "Your queue rear element is " + str(queue[-1]) +" .")
        input("Enter any key to close: ")
        queue_rear()


    """)
    input(style.RED + "Enter any key to close: ")
    queue_rear()


def queue_rear():
    print(style.YELLOW + """
    [+] The "rear" element of the queue is the element that was last pushed and will be the first to be popped.
        The "bottom" element of the queue is the one that, when removed, will leave the queue empty.
            1: Check the rear element in your created queue
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        queue_rear_check()
    elif selection == '2':
        queue_rear_review()
    elif selection == '3':
        queue_implementaion.queue_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        queue_rear()

