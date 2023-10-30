import os
import queue_dsa
import queue_creating
import enqueue
import dequeue
import queue_peak
import queue_rear
import queue_empty
import queue_size
queue_dsa
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





def queue_implementaion():
    print(style.YELLOW + """
    [+] You can do really fantastic opreations with Queue as bellow:
        1: creating Queue
        2: enqueue
        3: dequeue
        4: peak
        5: rear
        6: is_full
        7: is_empty
        8: size
        9: close
    """)
    stack_implementaion_selection = input(style.YELLOW + "Enter your selection:")
    if stack_implementaion_selection == '1':
        queue_creating.queue_creating()
    elif stack_implementaion_selection == '2':
        enqueue.queue_push()
    elif stack_implementaion_selection == '3':
        dequeue.queue_pop()
    elif stack_implementaion_selection == '4':
        queue_peak.queue_top()
    elif stack_implementaion_selection == '5':
        queue_rear.queue_rear()
    elif stack_implementaion_selection == '6':
        queue_empty.queue_empty()
    elif stack_implementaion_selection == '7':
        queue_empty.queue_empty()
    elif stack_implementaion_selection == '8':
        queue_size.queue_size()
    elif stack_implementaion_selection == '9':
        queue_dsa.test()
    else:
        queue_implementaion()