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
# implementation of the code
# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)


# selection sorting
def quick_sorting():
    print(style.CYAN + "Create your array first.")
    try:
        quick_array = []
        array_size = eval(input("Enter the size of your array: "))
        for i in range(array_size):
            array_element = eval(input("Enter the " + str(i) + " element of your array: "))
            quick_array.append(array_element)
        print("Your unsorted array is " + str(quick_array) + " .")
        N = len(quick_array)-1
        quicksort(quick_array, 0, N)
        print("your Sorted array is: ")
        for i in range(len(quick_array)):
            print("%d" % quick_array[i], end=" , ")

        back_select = input(style.RED + "For review press 0 on any other key to close: ")
        if back_select == '0':
            quick_sorting()
        else:
            quick_sort()
    except:
        print("invalid input")
        quick_sorting()


# code review
def quick_sort_code():
    print(style.WHITE + """
    # implementation of the code
# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)



    """)
    back_selection = input(style.RED + "Enter any key to exit: ")
    if back_selection == "0":
        quick_sort()
    else:
        quick_sort()


def quick_sort():
    print(style.CYAN + """
    [+] Select an option:
        1: code review
        2: implementaion
        3: back
    """)
    selection = input("Enter youre selection: ")
    if selection == '1':
        quick_sort_code()
    elif selection == '2':
        quick_sorting()
    elif selection == '3':
        sorting_array.array_sorting()
    else:
        print(style.RED + "[+] Invalid input try again")
        quick_sort()