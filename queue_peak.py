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


def queue_top_check():
    queue = queue_creating.queue_return()
    if queue == []:
        print(style.RED + "Your queue is empty")
        input("Enter any key to close: ")
        queue_top()
    else:
        print(style.RED + "Your queue peak element is " + str(queue[0]) + " .")
        input("Enter any key to close: ")
        queue_top()


def queue_top_review():
    print(style.WHITE + """
    def queue_top_check():
    queue = queue_creating.queue_return()
    if queue == []:
        print(style.RED + "Your queue is empty")
        input("Enter any key to close: ")
        queue_top()
    else:
        print(style.RED + "Your queue top element is " + str(queue[-1]) +" .")
        input("Enter any key to close: ")
        queue_top()


    """)
    input(style.RED + "Enter any key to close: ")
    queue_top()


def queue_top():
    print(style.YELLOW + """
    [+] The "peak" element of the queue is the element that was first enqued and will be the first to be dequed.
            1: Check the top element in your created queue
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        queue_top_check()
    elif selection == '2':
        queue_top_review()
    elif selection == '3':
        queue_implementaion.queue_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        queue_top()

