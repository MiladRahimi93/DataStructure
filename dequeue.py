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

queue = queue_creating.queue_return()
def queue_pop_process():

    if queue == []:
        print(style.RED + "Your queue is Empty!")
        queue_pop()
    else:
        print(style.YELLOW + "Your queue before dequeue process is " + str(queue) + " .")
        print("your queue after dequeue process is " + str(queue[1:]) + " .")
        select = input(style.RED + "Enter 0 for trying again or other key to close: ")
        if select == '0':
            queue_pop_process()
        else:
            queue_pop()
# code review
def queue_pop_review():

    print(style.WHITE + """
    # process

def queue_pop_process():
    queue = queue_creating.queue_return()
    if queue == []:
        print(style.RED + "Your queue is Empty!")
        queue_pop()
    else:
        print(style.YELLOW + "Your queue before poping is " + str(queue) + " .")
        queue = queue[:len(queue-1)]
        print("your queue after poping is " + str(queue) + " .")
        select = input(style.RED + "Enter 0 for trying again or other key to close: ")
        if select == '0':
            queue_pop_process()
        else:
            queue_pop()
    """)
    back_selection = input(style.RED +"""Enter any key to close: """)
    queue_pop()




def queue_pop():
    print(style.YELLOW + """
    [+] In dequeue process you will remove element at the top of your queue (FIFO).
            1: Dequeu process in queue check
            2: code review
            3: back
            """)
    selection = input("Enter your selection: ")
    if selection == '1':
        queue_pop_process()
    elif selection == '2':
        queue_pop_review()
    elif selection == '3':
        queue_implementaion.queue_implementaion()
    else:
        print(style.RED + "[+] invalid input try again!")
        queue_pop()

