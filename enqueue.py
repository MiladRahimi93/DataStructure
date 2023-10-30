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

def queue_pushing_process():
        queue = queue_creating.queue_return()
        print(style.YELLOW + "Your queue before enqueue is " + str(queue) + " .")
        pushing_element = input("Enter the element for enqueue: ")
        queue.append(pushing_element)
        print("your queue after enque process is " + str(queue) + " .")
        select = input(style.RED + "Enter 0 for trying again or other key to close: ")
        if select == '0':
            queue_pushing_process()
        else:
            queue_push()
# code review
def queue_push_review():

    print(style.WHITE + """
    # process

def queue_pushing_process():
    queue = queue_creating.queue_return()
    if queue == []:
        print(style.RED + "Your queue is empty")
        input("Enter any key to close: ")
        queue_push()
    else:
        print(style.RED + "Your queue before pushing is " + str(queue) + " .")
        pushing_element = input("Enter the element for pushing: ")
        queue = queue.append(pushing_element)
        input("your queue after pushing is " + str(queue) + " .")
        select = input(style.RED + "Enter a 0 for trying again or other key to close: ")
        if select == '0':
            queue_pushing_process()
        else:
        queue_empty()

    """)
    back_selection = input(style.RED +"""Enter any key to close: """)
    if back_selection == '0':
        queue_push()
    else:
        queue_push()




def queue_push():
    print(style.YELLOW + """
    [+] In enque process you will add element at the top of your queue (FIFO).
            1: enque process check
            2: enque code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        queue_pushing_process()
    elif selection == '2':
        queue_push_review()
    elif selection == '3':
        queue_implementaion.queue_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        queue_push()

