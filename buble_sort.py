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
def buble_sorting():
    print(style.CYAN + "Create your array first.")
    try:
        buble_array = []
        array_size = eval(input("Enter the size of your array: "))
        for i in range(array_size):
            array_element = eval(input("Enter the " + str(i) + " element of your array: "))
            buble_array.append(array_element)
        print("Your unsorted array is " + str(buble_array) + " .")
        # Traverse through all array elements
        n = len(buble_array)

        # Traverse through all array elements
        for i in range(n):
            swapped = False

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if buble_array[j] > buble_array[j + 1]:
                    buble_array[j], buble_array[j + 1] = buble_array[j + 1], buble_array[j]
                    swapped = True
            if (swapped == False):
                break
                # Driver code to test above
        print("your Sorted array is: ")
        for i in range(len(buble_array)):
            print("%d" % buble_array[i], end=" , ")

        back_select = input(style.RED + "For review press 0 on any other key to close: ")
        if back_select == '0':
            buble_sorting()
        else:
            buble_sort()
    except:
        print("invalid input")
        buble_sorting()


# code review
def buble_sort_code():
    print(style.WHITE + """
def buble_sorting():
    print(style.CYAN + "Create your array first.")
    try:
        buble_array = []
        array_size = eval(input("Enter the size of your array: "))
        for i in range(array_size):
            array_element = eval(input("Enter the " + str(i) + " element of your array: "))
            buble_array.append(array_element)
        print("Your unsorted array is " + str(buble_array) + " .")
        # Traverse through all array elements
        n = len(buble_array)

        # Traverse through all array elements
        for i in range(n):
            swapped = False

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if buble_array[j] > buble_array[j + 1]:
                    buble_array[j], buble_array[j + 1] = buble_array[j + 1], buble_array[j]
                    swapped = True
            if (swapped == False):
                break
                # Driver code to test above
        print("your Sorted array is: ")
        for i in range(len(buble_array)):
            print("%d" % buble_array[i], end=" , ")

        back_select = input(style.RED + "For review press 0 on any other key to close: ")
        if back_select == '0':
            buble_sorting()
        else:
            buble_sort()
    except:
        print("invalid input")
        buble_sorting()

    """)
    back_selection = input(style.RED + "Enter any key to exit: ")
    if back_selection == "0":
        buble_sort()
    else:
        buble_sort()


def buble_sort():
    print(style.CYAN + """
    [+] Select an option:
        1: code review
        2: implementaion
        3: back
    """)
    selection = input("Enter youre selection: ")
    if selection == '1':
        buble_sort_code()
    elif selection == '2':
        buble_sorting()
    elif selection == '3':
        sorting_array.array_sorting()
    else:
        print(style.RED + "[+] Invalid input try again")
        buble_sort()