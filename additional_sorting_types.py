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
def additional_types():
   print(style.GREEN + """"
   [+] Here are the addtional sorting tyoes that you can check:
        1: Radix Sort
        2: Bucket Sort
        3: Bingo Sort Algorithm
        4: ShellSort
        5: TimSort
        6: Comb Sort
        7: Pigeonhole Sort
        8: Cycle Sort
        9: Cocktail Sort
        10: Strand Sort
        11: Bitonic Sort
        12: Pancake sorting
        13: BogoSort or Permutation Sort
        14: Gnome Sort
        15: Sleep Sort – The King of Laziness
        16: Structure Sorting in C++
        17: Stooge Sort
        18: Tag Sort (To get both sorted and original)
        19: Tree Sort
        20: Odd-Even Sort / Brick Sort
        21: 3-way Merge Sort
   """)
   print(style.RED + "[+] Fore more information you can visit https://www.geeksforgeeks.org/sorting-algorithms/")
   back_selection = input("Enter any key to close: ")
   if back_selection == '0':
       sorting_array.array_sorting()
   else:
       sorting_array.array_sorting()