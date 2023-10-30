import os
import Array
import linked_list
import queue_dsa
import main
import stack
import queue
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

def linear_data_description():
        os.system('cls')
        print(style.GREEN + """         
        A linear data structure is known as a data structure that allows data elements to be arranged in a sequential or 
        linear fashion.Each element is attached with its next and previous adjacent.
        A linear data structure only has one level and performs linear searching in the data structure.""")
        print(style.YELLOW + """
        These are the types of linear DSA 1. Array 2. Stack 3. Queue 4: Linked List""")
        back = input(style.RED + "Press 0 to Return: ")
        if back == '0':
            test()
        else:
            linear_data_description()
# linear DSA implementation
def lineardsa_implementaion():
    print(style.BLUE +"""
    [+]Select and option from bellow for more information:
            1. Array
            2. Stack
            3. Queue
            4. Linked List
            5. Back""")
    linear_Dsa_selection = input(style.BLUE + "Enter your Selection: ")
    if linear_Dsa_selection == '1':
        os.system('cls')
        Array.test()
    elif linear_Dsa_selection == '2':
        os.system('cls')
        stack.test()
    elif linear_Dsa_selection == '3':
        os.system('cls')
        queue_dsa.test()
    elif linear_Dsa_selection == '4':
        os.system('cls')
        linked_list.test()
    elif linear_Dsa_selection == '5':
        os.system('cls')
        test()
    else:
        print(style.RED + "Invalid input!!!")
        lineardsa_implementaion()

def test():
        print(style.CYAN + """ 
        [+] Select and option from bellow:
            1: Linear Data structure Description
            2: Linear Data structure Types and Implementation
            3: Back""")
        linear_selection = input(style.CYAN + "Enter your Selection: ")
        if linear_selection == '1':
            linear_data_description()
        elif linear_selection == '2':
            lineardsa_implementaion()
        elif linear_selection == '3':
            main.Dsa_implementaion()
        else:
            print(style.RED + "+++Invlaid input+++")
            test()

