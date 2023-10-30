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
# traverse data algorithm process
def traverse_algo_print():
    print(style.CYAN + """
            Step 01: Start
            Step 02: [Initialize counter variable. ] Set i = LB.
            Step 03: Repeat for i = LB to UB.
            Step 04: Apply process to arr[i].
            Step 05: [End of loop. ]
            Step 06: Stop""")
    close_traverse_algo = input(style.CYAN + "Enter 0 to go back: ")
    if close_traverse_algo == '0':
        array_traversal()
    else:
        traverse_algo_print()

# opreation of array traversing
def array_traversing():
    traverse_array = []
    print(style.YELLOW + """create your array for traversing.""")
    try:
        size_of_traverse_array = eval(input(style.YELLOW + "Enter the size of your array: "))
        for i in range(size_of_traverse_array):
            array_element = input("Enter the " + str(i) + " element of array: ")
            traverse_array.append(array_element)
        for i in range(len(traverse_array)):
            print("the " + str(i) + " Element in array is " + str(traverse_array[i]))
        travese_back = input(style.RED + "Enter the 0 for back or other key for trying again")
        if travese_back == '0':
            array_implementaion.array_implementaion()
        else:
            array_traversing()
    except:
        print(style.RED + "[+] Invalid input")
        array_traversing()

# start of traversal
def array_traversal():
    print(style.CYAN + """
    [+]Traversal operation in array or simply traversing an array means,
    Accessing or printing each element of an array exactly once so that the data items (values)
    of the array can be checked or used as part of some other operation or process (This accessing and
    processing is sometimes called “visiting” the array).
        
        1: traversing array data structure algorithm
        2: opreation of array traversing
        3: Back""")
    travers_array_selection = input("Enter and option: ")
    if travers_array_selection == '1':
         traverse_algo_print()
    elif travers_array_selection == '2':
         array_traversing()
    elif travers_array_selection == '3':
         array_implementaion.array_implementaion()
    else:
        array_traversal()


