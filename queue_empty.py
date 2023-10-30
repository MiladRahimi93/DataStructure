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
# process

def queue_is_empty():
    queue = queue_creating.queue_return()
    if queue == []:
        print(style.RED + "Your queue is empty")
        input("Enter any key to close: ")
        queue_empty()
    else:
        print(style.RED + "Your queue is full.")
        input("Enter any key to close: ")
        queue_empty()
# code review
def queue_empty_review():

    print(style.WHITE + """
    # process    
    queue = queue_creating.queue_creation()
    def queue_is_empty():
    if queue == []:
        print("Your queue is empty")
        queue_empty()
    else:
        print("Your queue is full.")
        queue_empty()
    """)
    back_selection = input(style.RED +"""Enter any key to close: """)
    if back_selection == '0':
        queue_empty()
    else:
        queue_empty()




def queue_empty():
    print(style.YELLOW + """
    [+] Select an option if you didn't create queue before the process will return that queue is empty
        otherwise it will return that queue is full.
            1: queue is_full check
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        queue_is_empty()
    elif selection == '2':
        queue_empty_review()
    elif selection == '3':
        queue_implementaion.queue_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        queue_empty()

