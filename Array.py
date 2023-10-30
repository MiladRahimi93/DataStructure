import cv2
import  array_implementaion
import linear_dsa
import array_image
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

# int array creation implementation
def int_array_creation_implementaion():
    os.system('cls')
    int_array = []
    try:
        int_array_size = eval(input("enter size of your array: "))
        for i in range(int_array_size):
            try:
                int_array_elements = int(input("Insert the "+str(i)+" element of your array in int:"))
                int_array.append(int_array_elements)
            except:
                print("invalid input you should insert a int datatype")
                int_array_creation()
        print(style.YELLOW + "your array is "+str(int_array))
        back_to_selection = input(style.RED + "press any key to Back: ")
        if back_to_selection == '0':
            test()
        else:
            print("invalid input")
            test()

    except:
        print("invalid input")
        int_array_creation()
# int array print
def int_array_implementation_print():
    os.system('cls')
    print(style.WHITE + """
# int array creation implementation
def int_array_creation_implementaion():
    int_array = []
    try:
        int_array_size = eval(input("enter size of your array: "))
        for i in range(int_array_size):
            try:
                int_array_elements = int(input("Insert the "+str(i)+" element of your array in int:"))
                int_array.append(int_array_elements)
            except:
                print("invalid input you should insert a int datatype")
                int_array_creation()
        print(style.YELLOW + "your array is "+str(int_array))
        back_to_selection = input(style.RED + "press any key to Back: ")
        if back_to_selection == '0':
            test()
        else:
            print("invalid input")
            test()

    except:
        print("invalid input")
        int_array_creation()""")
    back_to_array_creation = input(style.MAGENTA + "[+] press 0 to back")
    if back_to_array_creation == '0':
        int_array_creation()
    else:
        print("invalid input!!")
        int_array_implementation_print()

# int array creation
def int_array_creation():
    os.system('cls')
    print(style.YELLOW + """
    Select an option:
    1. Code review
    2. code implementation
    3. Back""")
    int_array_process_selection = input(style.YELLOW + " Enter your Selection: ")
    if int_array_process_selection == '1':
        int_array_implementation_print()
    elif int_array_process_selection == '2':
        int_array_creation_implementaion()
    elif int_array_process_selection == '3':
        array_creation()
    else:
        print(style.RED + "invalid input")
        int_array_creation()



# str array creation
# int array print
def str_array_implementation_print():
    os.system('cls')
    print(style.WHITE + """
def str_array_creation_implementation():

    str_array = []
    try:
        str_array_size = eval(input("enter size of your array: "))
        for i in range(str_array_size):
            try:
                str_array_elements = str(input("Insert the "+str(i)+" element of your array in string:"))
                str_array.append(str_array_elements)
            except:
                print("invalid input you should insert a int datatype")
                str_array_creation()
        print(style.YELLOW + "your array is "+str(str_array))
        back_to_selection = input(style.RED + "press any key to Back: ")
        if back_to_selection == '0':
            test()
        else:
            test()

    except:
        print("invalid input")
        int_array_creation()
""")
    back_to_array_creation = input(style.MAGENTA + "[+] press 0 to back")
    if back_to_array_creation == '0':
        str_array_creation()
    else:
        print("invalid input!!")
        str_array_implementation_print()

# str array creation

def str_array_creation_implementation():
    os.system('cls')

    str_array = []
    try:
        str_array_size = eval(input("enter size of your array: "))
        for i in range(str_array_size):
            try:
                str_array_elements = str(input("Insert the "+str(i)+" element of your array in string:"))
                str_array.append(str_array_elements)
            except:
                print("invalid input you should insert a int datatype")
                str_array_creation()
        print(style.YELLOW + "your array is "+str(str_array))
        back_to_selection = input(style.RED + "press any key to Back: ")
        if back_to_selection == '0':
            test()
        else:
            test()

    except:
        print("invalid input")
        int_array_creation()



# str array creation
def str_array_creation():
    os.system('cls')
    print(style.YELLOW + """
    Select an option:
    1. Code review
    2. code implementation
    3. Back""")
    str_array_process_selection = input(style.YELLOW + " Enter your Selection: ")
    if str_array_process_selection == '1':
        str_array_implementation_print()
    elif str_array_process_selection == '2':
        str_array_creation_implementation()
    elif str_array_process_selection == '3':
        array_creation()
    else:
        print(style.RED + "invalid input")
        str_array_creation()


# float array creation


def float_array_implementation_print():
    os.system('cls')
    print(style.WHITE + """
def float_array_creation_implementation():

    float_array = []
    try:
        float_array_size = eval(input("enter size of your array: "))
        for i in range(float_array_size):
            try:
                float_array_elements = float(input("Insert the "+str(i)+" element of your array in string:"))
                float_array.append(float_array_elements)
            except:
                print("invalid input you should insert a int datatype")
                float_array_creation()
        print(style.YELLOW + "your array is "+str(float_array))
        back_to_selection = input(style.RED + "press any key to Back: ")
        if back_to_selection == '0':
            test()
        else:
            test()

    except:
        print("invalid input")
        float_array_creation()

""")
    back_to_array_creation = input(style.MAGENTA + "[+] press 0 to back")
    if back_to_array_creation == '0':
        float_array_creation()
    else:
        print("invalid input!!")
        float_array_implementation_print()

# str array creation

def float_array_creation_implementation():
    os.system('cls')

    float_array = []
    try:
        float_array_size = eval(input("enter size of your array: "))
        for i in range(float_array_size):
            try:
                float_array_elements = float(input("Insert the "+str(i)+" element of your array in float type:"))
                float_array.append(float_array_elements)
            except:
                print("invalid input you should insert a int datatype")
                float_array_creation()
        print(style.YELLOW + "your array is "+str(float_array))
        back_to_selection = input(style.RED + "press any key to Back: ")
        if back_to_selection == '0':
            test()
        else:
            test()

    except:
        print("invalid input")
        float_array_creation()



# str array creation
def float_array_creation():
    os.system('cls')
    print(style.YELLOW + """
    Select an option:
    1. Code review
    2. code implementation
    3. Back""")
    float_array_process_selection = input(style.YELLOW + " Enter your Selection: ")
    if float_array_process_selection == '1':
        float_array_implementation_print()
    elif float_array_process_selection == '2':
        float_array_creation_implementation()
    elif str_array_process_selection == '3':
        array_creation()
    else:
        print(style.RED + "invalid input")
        float_array_creation()







# array all creation
def array_creation():
    os.system('cls')
    print(style.WHITE + """
    [+]Array is consist of elements that have a static size and index that start from 0
    now please select the type of yor array:""")
    array_type_selection = input(style.WHITE + "int(for integer), str(for string), float(for float) or 0 for back:")
    if array_type_selection == "int":
        int_array_creation()
    elif array_type_selection == "str":
        str_array_creation()
    elif array_type_selection == "float":
        float_array_creation()
    elif array_type_selection == '0':
        test()
    else:
        array_creation()





# defination of array
def defenation_of_array():
    os.system('cls')
    print(style.BLUE + """
    Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value. 
    Arrays are classified into two types based on their dimensions :
    single-dimensional and multi-dimensional. Logically, a single-dimensional array represents a linear collection of data,
    and a two-dimensional array represents a mathematical matrix. Similarly, a multidimensional array has multiple dimensions.""")
    defination_array_close = input(style.RED + "Enter 0 for back: ")
    if defination_array_close == '0':
        test()
    else:
        defenation_of_array()
# main Program
def test():
    os.system('cls')
    print(style.GREEN + """
    
    [+] Select an Option:
        1: Array Defination and Types
        2: Array creation
        3: Array implementation
        4: Array image
        5: Back
    """)
    array_selection = input(style.MAGENTA + "Enter you Selection:")
    if array_selection == '1':
        defenation_of_array()
    elif array_selection == '2':
        array_creation()
    elif array_selection =='3':
        array_implementaion.array_implementaion()
    elif array_selection == '4':
        img = cv2.imread('arrayimg.png', cv2.IMREAD_GRAYSCALE)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        test()
    elif array_selection == '5':
        linear_dsa.lineardsa_implementaion()
    else:
        test()
