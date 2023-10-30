import os
import array_implementaion
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

# Binary search
def binary_search():
    print(style.YELLOW + """
    Binary Search is a searching algorithm used in a sorted array. In this algorithm, the element is found by repeatedly
    dividing the search interval in half and deciding the next interval to find the element. This searching algorithm 
    has a time complexity of O(log2N) where ‘N’ is the length of the array.
    The only thing to note is that the array must be sorted in increasing or decreasing order.
    
    Note: The implementation will done in non linear Data structure lessons!
    """)
    back_selection = input(style.RED + "Enter any key for closing: ")
    if back_selection == '0':
        searching_array()
    else:
        searching_array()

# linear search implementaion
def linear_search_implementaion():
    print(style.YELLOW + "First create your array.")

    try:
        array_size = eval(input("Enter the size of your array: "))
        array_search = []
        for i in range(array_size):
            array_element = input("Enter the " + str(i) + " element of your array:")
            array_search.append(array_element)
        print(style.YELLOW + "your array is " + str(array_search) + " .")
        searching_element = input("Enter the element you want to search: ")
        element_index = -1
        for i in range(array_size):
            if array_search[i] == searching_element:
                element_index = i
            else:
                pass
        if element_index == -1:
            print(style.RED + "The element does not exist in array.")
        else:
            print(style.YELLOW + "The element index is " + str(element_index))
    except:
        print(style.RED + "[+]invalid input try again")
        linear_search_implementaion()
    back_selection = input("for try again press 0 or other key for back: ")
    if back_selection == "0":
        linear_search_implementaion()
    else:
        linear_search()

# linear search code implementaion
def linear_search_code_review():
    print(style.YELLOW + """
    # linear search implementaion
    def linear_search_implementaion():
        print(style.YELLOW + "First create your array.")

        try:
            array_size = eval(input("Enter the size of your array: "))
            array_search = []
            for i in range(array_size):
                array_element = input("Enter the " + str(i) + " element of your array:")
                array_search.append(array_element)
            print(style.YELLOW + "your array is " + str(array_search) + " .")
            searching_element = input("Enter the element you want to search: ")
            element_index = -1
            for i in range(array_size):
                if array_search[i] == searching_element:
                    element_index = i
                else:
                    pass
            if element_index == -1:
                print(style.RED + "The element does not exist in array.")
            else:
                print(style.YELLOW + "The element index is " + str(element_index))
        except:
            print(style.RED + "[+]invalid input try again")
            linear_search_implementaion()
        back_selection = input("for try again press 0 or other key for back: ")
        if back_selection == "0":
            linear_search_implementaion()
        else:
            linear_search()""")
    back_selection = input(style.RED + "[+] Enter any key to close")
    if back_selection == '0':
        linear_search()
    else:
        linear_search()



# linear search




def linear_search():
    print(style.YELLOW + """
    Linear Search is defined as a sequential search algorithm that starts at one end and goes through
    each element of a list until the desired element or group of elements is found. Otherwise, the 
    search continues till the end of the data set. This has a time complexity of O(N) where ‘N’ is the
    length of the array.
    
    1: Code review
    2: Code implementation
    3: Back
    """)
    linear_search_selection = input("Enter your selection: ")
    if linear_search_selection == '1':
        linear_search_code_review()
    elif linear_search_selection == "2":
        linear_search_implementaion()
    elif linear_search_selection == "3":
        searching_array()
    else:
        print(style.RED + "[+] invalid input try again")
        linear_search()

# trinary search
def trinary_search():
    print(style.YELLOW + """
    Ternary search is a divide and conquer algorithm that can be used to find an element in an array.  
    It is similar to binary search where we divide the array into two parts but in this algorithm,
    we divide the given array into three parts and determine which has the key (searched element). 
    This algorithm also has the constraint that the array must be sorted.
    The time complexity for this algorithm is O(log3N) where ‘N’ is the size of the array.
    
    Note: The implementation will done in non linear Data structure lessons!
    """)
    back_selection = input(style.RED + "Enter any key for closing: ")
    if back_selection == '0':
        searching_array()
    else:
        searching_array()


def searching_array():
    print(style.YELLOW + """
    Searching is one of the most common operations performed in an array.
    Array searching can be defined as the operation of finding a particular element or a group of elements in the array.
    There are several searching algorithms. The most commonly used among them are:
        1: Linear Search
        2: Binary Search
        3: Ternary Search
        4: Back
    """)

    searching_selection = input('Enter your selection for information: ')
    if searching_selection == '1':
        linear_search()
    elif searching_selection == '2':
        binary_search()
    elif searching_selection =='3':
        trinary_search()
    elif searching_selection == '4':
        array_implementaion.array_implementaion()
    else:
        print(style.RED + "[+]Invalid input")
        searching_array()