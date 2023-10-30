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


queue = queue_creating.queue_return()


# process
def queue_size_implement():
    if queue == []:
        print(style.RED + "Your queue size is 0 it mean it doesn't contain any element.")
        input("Enter any key to close: ")
        queue_size()
    else:
        queue_size_imp = len(queue)
        print(style.RED + "The size of your queue is " + str(queue_size_imp) + " .")
        input("Enter any key to close")
        queue_size()


# review
def queue_size_review():
    print(style.WHITE + """
    # process
def queue_size_implement():
    if queue == []:
        print(style.RED + "Your queue size is 0 it mean it doesn't contain any element.")
        input("Enter any key to close: ")
    else:
        queue_size_imp = len(queue)
        print(style.RED + "The size of your queue is " + str(queue_size_imp) + " .")
        input("Enter any key to close")
        queue_size()

    """)
    input(style.RED + "Enter any key to close: ")
    queue_size()


def queue_size():
    print(style.YELLOW + """
    [+] Check the size of your created queue:
            1: Created queue size
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        queue_size_implement()
    elif selection == '2':
        queue_size_review()
    elif selection == '3':
        queue_implementaion.queue_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        queue_size()

