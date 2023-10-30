import  array_implementaion
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
# start of array deletion with index
def array_delete_index_implementaion():
    print(style.GREEN + """first create your array""")
    deletion_array = []
    try:
        array_size = eval(input("enter the size of your array: "))
        for i in range(array_size):
            array_element = input("Enter your Array" + str(i) + " Element: ")
            deletion_array.append(array_element)
        print(style.MAGENTA + "your array is " + str(deletion_array) + " .")
        try:
            deletion_index = eval(input("Enter the index of deleting element: "))
            if deletion_index < array_size and deletion_index > 0:
                deletion_array = deletion_array[:deletion_index] + deletion_array[deletion_index+1:]
                print(style.MAGENTA + "now your array is " + str(deletion_array) + " .")
                deletion_back = input(style.RED + "[-] Enter any key for closing: ")
                if deletion_back == '0':
                    array_delete_index()
                else:
                    array_delete_index()
            else:
                print("invalid index selected input")
                array_delete_index_implementaion()
        except:
            print(style.RED + "[+]invalid input")
            array_delete_index()
    except:
        print(style.RED + "[-] invalid input")
        array_delete_index()
# array deletion code review
def array_delete_index_review():
    print(style.WHITE + """
    # start of array deletion with index
def array_delete_index_implementaion():
    print(style.GREEN + "first create your array")
    deletion_array = []
    try:
        array_size = eval(input("enter the size of your array: "))
        for i in range(array_size):
            array_element = input("Enter your Array" + str(i) + " Element: ")
            deletion_array.append(array_element)
        print(style.MAGENTA + "your array is " + str(deletion_array) + " .")
        try:
            deletion_index = eval(input("Enter the index of deleting element: "))
            deletion_array = deletion_array[:deletion_index] + deletion_array[deletion_index+1:]
            print(style.MAGENTA + "now your array is " + str(deletion_array) + " .")
            deletion_back = input(style.RED + "[-] Enter any key for closing: ")
            if deletion_back == '0':
                array_delete_index()
            else:
                array_delete_index()
        except:
            print(style.RED + "[+]invalid input")
            array_delete_index()
    except:
        print(style.RED + "[-] invalid input")
        array_delete_index()""")
    back_selection = input(style.RED + "[-] Enter any key for back: ")
    if back_selection == '0':
        array_delete_index()
    else:
        array_delete_index()
# array deletion process
def array_delete_index():
    print(style.BLUE + """
    Select an option from bellow: 
        1: Code Review
        2: implementaion
        3: back""")
    selection_delete = input("Select an iption: ")
    if selection_delete == "1":
        array_delete_index_review()
    elif selection_delete == "2":
        array_delete_index_implementaion()
    elif selection_delete == "3":
        array_deletion()
    else:
        print(style.RED + "[+ invalid input]")
        array_delete_index()

# array deletion via element


def array_delete_element_implementaion():
    print(style.GREEN + """first create your array""")
    deletion_array = []
    # try:
    array_size = eval(input("enter the size of your array: "))
    for i in range(array_size):
            array_element = input("Enter your Array" + str(i) + " Element: ")
            deletion_array.append(array_element)
    print(style.MAGENTA + "your array is " + str(deletion_array) + " .")
    # try:
    deletion_element = input("Enter the element for deleting: ")
    for i in range(len(deletion_array)):
            if deletion_array[i] == deletion_element:
                    del deletion_array[i]
            else:
                    print()

    print(style.MAGENTA + "now your array is " + str(deletion_array) + " .")
    deletion_back = input(style.RED + "[-] Enter any key for closing: ")
    if deletion_back == '0':
            array_delete_element()
    else:
            array_delete_element()
    # except:
        #     print(style.RED + "[+]invalid input")
        #     array_delete_element()
    # except:
    #     print(style.RED + "[-] invalid input")
    #     array_delete_element()
# array deletion code review
def array_delete_element_review():
    print(style.WHITE + """
def array_delete_element_implementaion():
    print(style.GREEN + "first create your array")
    deletion_array = []
    try:
        array_size = eval(input("enter the size of your array: "))
        for i in range(array_size):
            array_element = input("Enter your Array" + str(i) + " Element: ")
            deletion_array.append(array_element)
        print(style.MAGENTA + "your array is " + str(deletion_array) + " .")
        try:
            deletion_element = eval(input("Enter the element for deleting: "))
            if deletion_element in deletion_array:
                deleletion_index = 0
                for i in range(array_size):
                    if deletion_array[i] == deletion_element:
                        deleletion_index = i
                    deletion_array = deletion_array[:deletion_index] + deletion_array[deletion_index+1:]
                print(style.MAGENTA + "now your array is " + str(deletion_array) + " .")
                deletion_back = input(style.RED + "[-] Enter any key for closing: ")
                if deletion_back == '0':
                    array_delete_element()
                else:
                    array_delete_element()
            else:
                print("invalid index selected input")
                array_delete_element_implementaion()
        except:
            print(style.RED + "[+]invalid input")
            array_delete_element()
    except:
        print(style.RED + "[-] invalid input")
        array_delete_element()""")
    back_selection = input(style.RED + "[-] Enter any key for back: ")
    if back_selection == '0':
        array_delete_element()
    else:
        array_delete_element()
# array deletion process
def array_delete_element():
    print(style.BLUE + """
    Select an option from bellow: 
        1: Code Review
        2: implementaion
        3: back""")
    selection_delete = input("Select an iption: ")
    if selection_delete == "1":
        array_delete_element_review()
    elif selection_delete == "2":
        array_delete_element_implementaion()
    elif selection_delete == "3":
        array_deletion()
    else:
        print(style.RED + "[+ invalid input]")
        array_delete_element()


# start of process
def array_deletion():
    print(style.MAGENTA + """
    In an array you can delete and element via its index of element itself as bellow you can check:
    1: Delete with index
    2: Delete with element value
    3: Back""")
    array_deletion_select = input("Enter your choice:")
    if array_deletion_select == '1':
        array_delete_index()
    elif array_deletion_select == '2':
        array_delete_element()
    elif array_deletion_select == '3':
        array_implementaion.array_implementaion()
    else:
        print(style.RED + "[+] invalid input")