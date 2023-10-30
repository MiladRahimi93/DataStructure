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
def countsort(input_array):
    # Finding the maximum element of input_array.
    M = max(input_array)

    # Initializing count_array with 0
    count_array = [0] * (M + 1)

    # Mapping each element of input_array as an index of count_array
    for num in input_array:
        count_array[num] += 1

    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    # Creating output_array from count_array
    output_array = [0] * len(input_array)

    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1

    return output_array



# selection sorting
def counting_sorting():
    print(style.CYAN + "Create your array first.")
    try:
        counting_array = []
        array_size = eval(input("Enter the size of your array: "))
        for i in range(array_size):
            array_element = eval(input("Enter the " + str(i) + " element of your array: "))
            counting_array.append(array_element)
        print("Your unsorted array is " + str(counting_array) + " .")
        # Traverse through all array elements
        counting_array = countsort(counting_array)
        print("your Sorted array is: ")
        for i in range(len(counting_array)):
            print("%d" % counting_array[i], end=" , ")

        back_select = input(style.RED + "For review press 0 on any other key to close: ")
        if back_select == '0':
            counting_sorting()
        else:
            count_sort()
    except:
        print("invalid input")
        counting_sorting()


# code review
def count_sort_code():
    print(style.WHITE + """def count_sort(input_array):
    # Finding the maximum element of input_array.
    M = max(input_array)
 
    # Initializing count_array with 0
    count_array = [0] * (M + 1)
 
    # Mapping each element of input_array as an index of count_array
    for num in input_array:
        count_array[num] += 1
 
    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
 
    # Creating output_array from count_array
    output_array = [0] * len(input_array)
 
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
 
    return output_array
    """)
    back_selection = input(style.RED + "Enter any key to exit: ")
    if back_selection == "0":
        count_sort()
    else:
        count_sort()


def count_sort():
    print(style.CYAN + """
    [+] Select an option:
        1: code review
        2: implementaion
        3: back
    """)
    selection = input("Enter youre selection: ")
    if selection == '1':
        count_sort_code()
    elif selection == '2':
        counting_sorting()
    elif selection == '3':
        sorting_array.array_sorting()
    else:
        print(style.RED + "[+] Invalid input try again")
        count_sort()