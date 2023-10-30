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
# Begining array insertion code review
def beginig_insertion_code():
    print(style.WHITE + """    
    print(style.CYAN + "Create your array first.")
    insert_array = []
    try:
        array_size = eval(input("enter the size of your array:"))
        for i in range(array_size):
            array_element = input("enter the " + str(i) + " element of your array: ")
            insert_array.append(array_element)
        print("your array is " + str(insert_array) + " .")
        inserting_element = input("now insert the element you want to add at the begining of your array: ")
        insert_array = [inserting_element] + insert_array
        print("now your array is " + str(insert_array) + " .")
        insertion_menue = input(style.RED + "Enter any key to back menue: ")
        if insertion_menue == '0':
            array_insertion()
        else:
            array_insertion()

    except:
        print(style.RED + "invalid input enter an int.")
        begining_insertion()""")
    back_selection = input(style.RED + "enter any key to go back: ")
    if back_selection == '0':
        begining_insertion()
    else:
        begining_insertion()


# begining insertion implementation

def begining_insertion_implementation():

    print(style.CYAN + "Create your array first.")
    insert_array = []
    try:
        array_size = eval(input("enter the size of your array:"))
        for i in range(array_size):
            array_element = input("enter the " + str(i) + " element of your array: ")
            insert_array.append(array_element)
        print("your array is " + str(insert_array) + " .")
        inserting_element = input("now insert the element you want to add at the begining of your array: ")
        insert_array = [inserting_element] + insert_array
        print("now your array is " + str(insert_array) + " .")
        insertion_menue = input(style.RED + "Enter any key to back menue: ")
        if insertion_menue == '0':
            array_insertion()
        else:
            array_insertion()

    except:
        print(style.RED + "invalid input enter an int.")
        begining_insertion()

# Beginning insertion
def begining_insertion():
    print(style.CYAN + """"
    Select an option from bellow:
    1: Code review
    2: code implementation
    3: Back""")
    insertion_selection = input(style.CYAN + "Enter your choice:")
    if insertion_selection == '1':
        beginig_insertion_code()
    elif insertion_selection == '2':
        begining_insertion_implementation()
    elif insertion_selection == '3':
        array_insertion()
    else:
        print(style.RED + "invalid input")
        begining_insertion()

# End of array insertion implementaion
# Begining array insertion code review
def end_insertion_code():
    print(style.WHITE + """
    print(style.CYAN + "Create your array first.")
    insert_array = []
    try:
        array_size = eval(input("enter the size of your array:"))
        for i in range(array_size):
            array_element = input("enter the " + str(i) + " element of your array: ")
            insert_array.append(array_element)
        print("your array is " + str(insert_array) + " .")
        inserting_element = input("now insert the element you want to add at the end of your array: ")
        insert_array =  insert_array + [inserting_element]
        print("now your array is " + str(insert_array) + " .")
        insertion_menue = input(style.RED + "Enter any key to back menue: ")
        if insertion_menue == '0':
            array_insertion()
        else:
            array_insertion()

    except:
        print(style.RED + "invalid input enter an int.")
        begining_insertion()
""")
    back_selection = input(style.RED + "enter any key to go back: ")
    if back_selection == '0':
        end_insertion()
    else:
        end_insertion()


# begining insertion implementation

def end_insertion_implementation():

    print(style.CYAN + "Create your array first.")
    insert_array = []
    try:
        array_size = eval(input("enter the size of your array:"))
        for i in range(array_size):
            array_element = input("enter the " + str(i) + " element of your array: ")
            insert_array.append(array_element)
        print("your array is " + str(insert_array) + " .")
        inserting_element = input("now insert the element you want to add at the end of your array: ")
        insert_array =  insert_array + [inserting_element]
        print("now your array is " + str(insert_array) + " .")
        insertion_menue = input(style.RED + "Enter any key to back menue: ")
        if insertion_menue == '0':
            array_insertion()
        else:
            array_insertion()

    except:
        print(style.RED + "invalid input enter an int.")
        begining_insertion()

# Beginning insertion
def end_insertion():
    print(style.CYAN + """"Select an option from bellow:
    1: Code review
    2: code implementation
    3: Back""")
    insertion_selection = input(style.CYAN + "Enter your choice:")
    if insertion_selection == '1':
        end_insertion_code()
    elif insertion_selection == '2':
        end_insertion_implementation()
    elif insertion_selection == '3':
        array_insertion()
    else:
        print(style.RED + "invalid input")
        end_insertion()

# insertion after an index
# Begining array insertion code review
def random_insertion_code():
    print(style.WHITE + """

def random_insertion_implementation():

    print(style.CYAN + "Create your array first.")
    insert_array = []
    try:
        array_size = eval(input("enter the size of your array:"))
        for i in range(array_size):
            array_element = input("enter the " + str(i) + " element of your array: ")
            insert_array.append(array_element)
        print("your array is " + str(insert_array) + " .")
        inserting_element = input("now insert the element you want to add at the end of your array: ")
        try:
            inserting_element_index = eval(input("enter the index of element you want to add after:"))
            insert_array =  insert_array[:inserting_element_index] + [inserting_element] + [inserting_element_index + 1]            
        except:
            print('invalid in array size')
            random_insertion_implementation()
        print("now your array is " + str(insert_array) + " .")
        insertion_menue = input(style.RED + "Enter any key to back menue: ")
        if insertion_menue == '0':
            array_insertion()
        else:
            array_insertion()

    except:
        print(style.RED + "invalid input enter an int.")
        begining_insertion()
""")
    back_selection = input(style.RED + "enter any key to go back: ")
    if back_selection == '0':
        default_insertion()
    else:
        default_insertion()


# begining insertion implementation

def random_insertion_implementation():

    print(style.CYAN + "Create your array first.")
    insert_array = []
    try:
        array_size = eval(input("enter the size of your array:"))
        for i in range(array_size):
            array_element = input("enter the " + str(i) + " element of your array: ")
            insert_array.append(array_element)
        print("your array is " + str(insert_array) + " .")
        inserting_element = input("now insert the element you want to add in your array: ")
        try:
            inserting_element_index = eval(input("enter the index of element you want to add after:"))
            insert_array =  insert_array[:inserting_element_index] + [inserting_element] + insert_array[inserting_element_index:]
        except:
            print('invalid in array size')
            random_insertion_implementation()
        print("now your array is " + str(insert_array) + " .")
        insertion_menue = input(style.RED + "Enter any key to back menue: ")
        if insertion_menue == '0':
            array_insertion()
        else:
            array_insertion()

    except:
        print(style.RED + "invalid input enter an int.")
        begining_insertion()

# Beginning insertion
def default_insertion():
    print(style.CYAN + """"
    Select an option from bellow:
    1: Code review
    2: code implementation
    3: Back""")
    insertion_selection = input(style.CYAN + "Enter your choice:")
    if insertion_selection == '1':
        random_insertion_code()
    elif insertion_selection == '2':
        random_insertion_implementation()
    elif insertion_selection == '3':
        array_insertion()
    else:
        print(style.RED + "invalid input")
        default_insertion()



# start of array insertion
def array_insertion():
    print(style.YELLOW + """
    You can insert data in your created array following you can select and option.
        1: insertion in begining of array
        2: insertion at the end of an array
        3: insertion after an specific index
        4: Back""")
    insertion_selection = input(style.YELLOW + "Enter your selection: ")
    if insertion_selection == '1':
        begining_insertion()
    elif insertion_selection == '2':
        end_insertion()
    elif insertion_selection == '3':
        default_insertion()
    elif insertion_selection == '4':
        array_implementaion.array_implementaion()
    else:
        print(style.RED + "[+] invalid input")
        array_insertion()
