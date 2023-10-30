import os

import linear_dsa
import stack_empty
import creating_stack
import stack
import stack_size
import stack_top
import stack_push
import stack_pop
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





def stack_implementaion():
    print(style.YELLOW + """
    [+] You can do really fantastic opreations with stack as bellow:
        1: creating stack
        2: is_empty
        3: size
        4: top
        5: push
        6: pop
        7: Back
    """)
    stack_implementaion_selection = input(style.YELLOW + "Enter your selection:")
    if stack_implementaion_selection == '1':
        creating_stack.stack_creating()
    elif stack_implementaion_selection == '2':
        stack_empty.stack_empty()
    elif stack_implementaion_selection == '3':
        stack_size.stack_size()
    elif stack_implementaion_selection == '4':
        stack_top.stack_top()
    elif stack_implementaion_selection == '5':
        stack_push.stack_push()
    elif stack_implementaion_selection == '6':
        stack_pop.stack_pop()
    elif stack_implementaion_selection == '7':
        linear_dsa.test()