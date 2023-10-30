import cv2
import linear_dsa
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
# stack definiation
def defenation_of_queue():
    print(style.GREEN + """
    [+] A Queue is defined as a linear data structure that is open at both ends and the operations are performed in
        First In First Out (FIFO) order.
        FIFO Principle of Queue:
        A Queue is like a line waiting to purchase tickets, where the first person in line is the first person served.
        (i.e. First come first serve).
        Position of the entry in a queue ready to be served, that is, the first entry that will be removed from the 
        queue, is called the front of the queue(sometimes, head of the queue), similarly, the position of the last 
        entry in the queue, that is, the one most recently added, is called the rear (or the tail) of the queue.
        [+] Characteristics of Queue:
            1: Queue can handle multiple data.
            2: We can access both ends.
            3: They are fast and flexible. 
            4: Queue Representation:
            5: Like stacks, Queues can also be represented in an array: In this representation, the Queue is implemented
                using the array.
        
    """)
    back_select = input(style.RED + "Enter any key to close: ")
    test()


# main Program
def test():
    print(style.GREEN + """

    [+] Select an Option:
        1: Queue Defination
        2: Queue implementation
        3: Queue image
        4: Back
    """)
    stack_selection = input(style.MAGENTA + "Enter you Selection:")
    if stack_selection == '1':
        defenation_of_queue()
    elif stack_selection == '2':
        queue_implementaion.queue_implementaion()
    elif stack_selection == '3':
        img = cv2.imread('queue.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        test()
    elif stack_selection == '4':
        linear_dsa.lineardsa_implementaion()
    else:
        test()
