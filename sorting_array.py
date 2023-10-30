import os
import array_implementaion
import selection_sort
import buble_sort
import insertion_sort
import merge_sort
import quick_sort
import heap_sort
import counting_sort
import additional_sorting_types
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

def array_sorting():
    print(style.CYAN + """
    [+] A Sorting Algorithm is used to rearrange a given array or list of elements according to a comparison
    operator on the elements.
    The comparison operator is used to decide the new order of elements in the respective data structure.
        1: Selection Sort
        2: Bubble Sort
        3: Insertion Sort
        4: Merge Sort
        5: Quick Sort
        6: Heap Sort
        7: Counting Sort
        8: other types name
        9: Back
    """)
    selection_of_type = input("[+] Enter your selection: ")
    if selection_of_type == '1':
        selection_sort.selection_sort()
    elif selection_of_type == '2':
        buble_sort.buble_sort()
    elif selection_of_type == '3':
        insertion_sort.insertion_sort()
    elif selection_of_type == '4':
        merge_sort.merge_sort()
    elif selection_of_type == '5':
        quick_sort.quick_sort()
    elif selection_of_type == '6':
        heap_sort.heap_sort()
    elif selection_of_type == '7':
        counting_sort.count_sort()
    elif selection_of_type == '8':
        additional_sorting_types.additional_types()
    elif selection_of_type == '9':
        array_implementaion.array_implementaion()
    else:
        print(style.RED + "[+] invalid input")
        array_sorting()