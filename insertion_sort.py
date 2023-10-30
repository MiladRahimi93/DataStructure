import os
import sorting_array
import sys


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


# selection sorting
def insertion_sorting():
    print(style.CYAN + "Create your array first.")
    try:
        insertion_array = []
        array_size = eval(input("Enter the size of your array: "))
        for i in range(array_size):
            array_element = eval(input("Enter the " + str(i) + " element of your array: "))
            insertion_array.append(array_element)
        print("Your unsorted array is " + str(insertion_array) + " .")
        # Traverse through all array elements
        # Traverse through 1 to len(arr)
        for i in range(1, len(insertion_array)):

            key = insertion_array[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < insertion_array[j]:
                insertion_array[j + 1] = insertion_array[j]
                j -= 1
            insertion_array[j + 1] = key        # Driver code to test above
        print("your Sorted array is: ")
        for i in range(len(insertion_array)):
            print("%d" % insertion_array[i], end=" , ")

        back_select = input(style.RED + "For review press 0 on any other key to close: ")
        if back_select == '0':
            insertion_sorting()
        else:
            insertion_sort()
    except:
        print("invalid input")
        insertion_sorting()


# code review
def insertion_sort_code():
    print(style.WHITE + """def insertion_sorting():
    print(style.CYAN + "Create your array first.")
    try:
        insertion_array = []
        array_size = eval(input("Enter the size of your array: "))
        for i in range(array_size):
            array_element = eval(input("Enter the " + str(i) + " element of your array: "))
            insertion_array.append(array_element)
        print("Your unsorted array is " + str(insertion_array) + " .")
        # Traverse through all array elements
        # Traverse through 1 to len(arr)
        for i in range(1, len(insertion_array)):

            key = insertion_array[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < insertion_array[j]:
                insertion_array[j + 1] = insertion_array[j]
                j -= 1
            insertion_array[j + 1] = key        # Driver code to test above
        print("your Sorted array is: ")
        for i in range(len(insertion_array)):
            print("%d" % insertion_array[i], end=" , ")

        back_select = input(style.RED + "For review press 0 on any other key to close: ")
        if back_select == '0':
            insertion_sorting()
        else:
            insertion_sort()
    except:
        print("invalid input")
        insertion_sorting()


    """)
    back_selection = input(style.RED + "Enter any key to exit: ")
    if back_selection == "0":
        insertion_sort()
    else:
        insertion_sort()


def insertion_sort():
    print(style.CYAN + """
    [+] Select an option:
        1: code review
        2: implementaion
        3: back
    """)
    selection = input("Enter youre selection: ")
    if selection == '1':
        insertion_sort_code()
    elif selection == '2':
        insertion_sorting()
    elif selection == '3':
        sorting_array.array_sorting()
    else:
        print(style.RED + "[+] Invalid input try again")
        insertion_sort()