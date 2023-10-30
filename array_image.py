import Array
import cv2
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

def array_image_load():

    try:
        # Load the image
        image = cv2.imread("arrayimg.png")

        # Display the image
        cv2.imshow("Image", image)
        input("Enter any key to back: ")
        Array.test()
    except:

        input("Not Exist!")
        Array.test()
