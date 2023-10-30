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
def selection_sorting():
    print(style.CYAN + "Create your array first.")
    try:
        selection_array = []
        array_size = eval(input("Enter the size of your array: "))
        for i in range(array_size):
            array_element = eval(input("Enter the " + str(i) + " element of your array: "))
            selection_array.append(array_element)
        print("Your unsorted array is " + str(selection_array) + " .")
        # Traverse through all array elements
        for i in range(len(selection_array)):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(selection_array)):
                if selection_array[min_idx] > selection_array[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            selection_array[i], selection_array[min_idx] = selection_array[min_idx], selection_array[i]

        # Driver code to test above
        print("your Sorted array is: ")
        for i in range(len(selection_array)):
            print("%d" % selection_array[i], end=" , ")

        back_select = input(style.RED + "For review press 0 on any other key to close: ")
        if back_select == '0':
            selection_sorting()
        else:
            selection_sort()
    except:
        print("invalid input")
        selection_sorting()
# code review
def selection_sort_code():
    print(style.WHITE + """
# selection sorting
def selection_sorting():
    print(style.CYAN + "Create your array first.")
    try:
        selection_array = []
        array_size = eval(input("Enter the size of your array: "))
        for i in range(array_size):
            array_element = eval(input("Enter the " + str(i) + " element of your array: "))
            selection_array.append(array_element)
        print("Your unsorted array is " + str(selection_array) + " .")
        # Traverse through all array elements
        for i in range(len(selection_array)):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(selection_array)):
                if selection_array[min_idx] > selection_array[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            selection_array[i], selection_array[min_idx] = selection_array[min_idx], selection_array[i]

        # Driver code to test above
        print("your Sorted array is: ")
        for i in range(len(selection_array)):
            print("%d" % selection_array[i], end=" , ")
    except:
        print("invalid input")
        selection_sorting()
    
    """)
    back_selection = input(style.RED + "Enter any key to exit: ")
    if back_selection == "0":
        selection_sort()
    else:
        selection_sort()



def selection_sort():
    print(style.CYAN + """
    [+] Select an option:
        1: code review
        2: implementaion
        3: back
    """)
    selection = input("Enter youre selection: ")
    if selection == '1':
        selection_sort_code()
    elif selection == '2':
        selection_sorting()
    elif selection == '3':
        sorting_array.array_sorting()
    else:
        print(style.RED + "[+] Invalid input try again")
        selection_sort()