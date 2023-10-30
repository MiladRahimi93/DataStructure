import  Array
import os
import array_traversal
import array_insertion
import array_deletion
import searching_array
import array_update
import sorting_array


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

 # start of implementaion


def array_implementaion():
    print(style.YELLOW + """[+] You can do really fantastic opreations with array as bellow:
    1: Traversal
    2: insertion
    3: Deletion
    4: Searching
    5: Update
    6: Sorting
    7: Back
    """)
    array_implementaion_selection = input(style.YELLOW + "Enter your selection:")
    if array_implementaion_selection == '1':
        array_traversal.array_traversal()
    elif array_implementaion_selection == '2':
        array_insertion.array_insertion()
    elif array_implementaion_selection == '3':
        array_deletion.array_deletion()
    elif array_implementaion_selection == '4':
        searching_array.searching_array()
    elif array_implementaion_selection == '5':
        array_update.array_update()
    elif array_implementaion_selection == '6':
        sorting_array.array_sorting()
    elif array_implementaion_selection == '7':
        Array.test()
    else:
        print(style.RED +"[+] Invalid input")
        array_implementaion()
