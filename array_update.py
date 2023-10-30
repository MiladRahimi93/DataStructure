import array_implementaion
import os
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

# process
def update_code_implementaion():
    print(style.GREEN + "First create your array.")

    try:
        array_size = eval(input("Enter the size of your array: "))
        array_update_list = []
        for i in range(array_size):
            array_element = input("Enter the " + str(i) + " element of your array:")
            array_update_list.append(array_element)
        print(style.GREEN + "your array is " + str(array_update_list) + " .")
        update_index = eval(input("Enter the index of element you want to update: "))
        update_element = input("Enter the value for updating selected index: ")
        array_update_list[update_index] = update_element
        print(style.GREEN + "Now your updated array is " + str(array_update_list) + " .")
        back_selection = input("Enter 0 for trying again or any other key to close: ")
        if back_selection == '0':
            update_code_implementaion()
        else:
            array_update()
    except:
        print(style.RED + "Invalid input try again the value should be integer.")
        update_code_implementaion()

# code review
def update_code_review():
    print(style.WHITE + """
    # process
def update_code_implementaion():
    print(style.GREEN + "First create your array.")

    try:
        array_size = eval(input("Enter the size of your array: "))
        array_update_list = []
        for i in range(array_size):
            array_element = input("Enter the " + str(i) + " element of your array:")
            array_update_list.append(array_element)
        print(style.GREEN + "your array is " + str(array_update_list) + " .")
        update_index = eval(input("Enter the index of element you want to update: "))
        update_element = input("Enter the value for updating selected index: ")
        array_update_list[update_index] = update_element
        print(style.GREEN + "Now your updated array is " + str(array_update_list) + " .")
        back_selection = input("Enter 0 for trying again or any other key to close: ")
        if back_selection == '0':
            update_code_implementaion()
        else:
            array_update()
    except:
        print(style.RED + "Invalid input try again the value should be integer.")
        update_code_implementaion()

    """)
    back_selection = input(style.RED + "Enter any key to close: ")
    if back_selection == '0':
        array_update()
    else:
        array_update()
# implementation
def array_update():
    print(style.GREEN + """
    [+] We can update an existing element in an array.
        1: code review
        2: implementation
        3: back
    """)
    update_selection = input("Enter your Selection: ")
    if update_selection == '1':
        update_code_review()
    elif update_selection == '2':
        update_code_implementaion()
    elif update_selection == '3':
        array_implementaion.array_implementaion()
    else:
        print(style.RED + "[+]invalid input try again")
        array_update()