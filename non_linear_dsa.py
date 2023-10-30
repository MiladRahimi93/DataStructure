import os
import graph_dsa
import tree

import main


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

def non_linear_data_description():
        os.system('cls')
        print(style.GREEN + """
        [+] A non-linear data structure is a type of data structure where the elements are not arranged in a sequential
        manner. In other words, the elements are not connected in a linear fashion such as a linked list or an array.
        Instead, the elements are organized in a hierarchical or network-like structure.
        
        Common examples of non-linear data structures include trees, graphs, and heaps. These data structures allow for more
        complex relationships between elements, making them suitable for solving various problems.
        
        Here are some links that provide more information about non-linear data structures:
        
        GeeksforGeeks: Non-linear Data Structures - https://www.geeksforgeeks.org/non-linear-data-structures/
        Tutorialspoint: Non-linear Data Structures - https://www.tutorialspoint.com/non_linear_data_structures/index.htm
        Data Structures and Algorithms - Non-Linear Data Structures - https://www.studytonight.com/data-structures/non-linear-data-structures
        If you have a specific code-related question about non-linear data structures, please provide more details, and I'll be happy to assist you further.
                """)
        back = input(style.RED + "Press 0 to Return: ")
        if back == '0':
            test()
        else:
            non_linear_data_description()
# non_linear DSA implementation
def non_lineardsa_implementaion():
    print(style.BLUE +"""
    [+]Select and option from bellow for more information:
            1. Tree
            2. Graph
            3. Back""")
    non_linear_Dsa_selection = input(style.BLUE + "Enter your Selection: ")
    if non_linear_Dsa_selection == '1':
        tree.test()
    elif non_linear_Dsa_selection == '2':
        graph_dsa.test()
    elif non_linear_Dsa_selection == '3':
        main.Dsa_implementaion()
    else:
        print(style.RED + "Invalid input!!!")
        non_lineardsa_implementaion()

def test():
        print(style.CYAN + """ 
        [+] Select and option from bellow:
            1: None_linear Data structure Description
            2: None_linear Data structure Types and Implementation
            3: Back""")
        non_linear_selection = input(style.CYAN + "Enter your Selection: ")
        if non_linear_selection == '1':
            non_linear_data_description()
        elif non_linear_selection == '2':
            non_lineardsa_implementaion()
        elif non_linear_selection == '3':
            main.Dsa_implementaion()
        else:
            print(style.RED + "+++Invlaid input+++")
            test()

