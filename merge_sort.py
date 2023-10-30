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
# Python program for implementation of MergeSort


def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# Into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1







# selection sorting
def merge_sorting():
    print(style.CYAN + "Create your array first.")
    try:
        merge_array = []
        array_size = eval(input("Enter the size of your array: "))
        for i in range(array_size):
            array_element = eval(input("Enter the " + str(i) + " element of your array: "))
            merge_array.append(array_element)
        print("Your unsorted array is " + str(merge_array) + " .")
        # Traverse through all array elements
        mergeSort(merge_array)
        print("your Sorted array is: ")
        for i in range(len(merge_array)):
            print("%d" % merge_array[i], end=" , ")

        back_select = input(style.RED + "For review press 0 on any other key to close: ")
        if back_select == '0':
            merge_sorting()
        else:
            merge_sort()
    except:
        print("invalid input")
        merge_sorting()


# code review
def merge_sort_code():
    print(style.WHITE + """
    
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# Into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


    """)
    back_selection = input(style.RED + "Enter any key to exit: ")
    if back_selection == "0":
        merge_sort()
    else:
        merge_sort()


def merge_sort():
    print(style.CYAN + """
    [+] Select an option:
        1: code review
        2: implementaion
        3: back
    """)
    selection = input("Enter youre selection: ")
    if selection == '1':
        merge_sort_code()
    elif selection == '2':
        merge_sorting()
    elif selection == '3':
        sorting_array.array_sorting()
    else:
        print(style.RED + "[+] Invalid input try again")
        merge_sort()