import os
import linear_dsa
import non_linear_dsa
import cv2
# System call

# Class of different styles

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



# Selection of Dsa type

def dsa_type_selection():
    type_selection = input(style.RED + "Enter your Selection: ")
    if type_selection == '1':
        linear_dsa.test()
    elif type_selection == '2':
        non_linear_dsa.test()
    elif type_selection == '3':
        img = cv2.imread('dsatypes.png', cv2.IMREAD_GRAYSCALE)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        dsa_type_selection()
    elif type_selection == '4':
        pass
    else:
        print("+++++INVALID INPUT TRY AGAIN+++++")
        dsa_type_selection()


def Dsa_implementaion():
    print(style.YELLOW + """
        ########################################################################################################################
    # ___       _             _               _                               _     _   _              _ _   _             #
    #|   \ __ _| |_ __ _   __| |_ _ _ _  _ __| |_ _  _ _ _ ___   __ _ _ _  __| |   /_\ | |__ _ ___ _ _(_) |_| |_  _ __  ___#
    #| |) / _` |  _/ _` | (_-<  _| '_| || / _|  _| || | '_/ -_) / _` | ' \/ _` |  / _ \| / _` / _ \ '_| |  _| ' \| '  \(_-<#
    #|___/\__,_|\__\__,_| /__/\__|_|  \_,_\__|\__|\_,_|_| \___| \__,_|_||_\__,_| /_/ \_\_\__, \___/_| |_|\__|_||_|_|_|_/__/#
    #                                                                                    |___/                             #
    ########################################################################################################################
    
    [+]This is program for easy to advance Data structure and Algorithms try to enjoy
        
        """)
    print(style.RED + " [+]for more information you can visit www.github.com/miladrahimi93")
    print(style.GREEN + """ [+]Data structure and algorithms:
     A data structure is a named location that can be used to store and organize data.
     And, an algorithm is a collection of steps to solve a particular problem.
     Learning data structures and algorithms allow us to write efficient and optimized computer programs.""")

    print(style.YELLOW + """    [+]These are the types of Datastructure and algorithms Select one for more information:
            1: Linear Datastructure
            2: None Linear Datastructure
            3: image Description
            4: close program""")
    dsa_type_selection()


if __name__ == '__main__':
    Dsa_implementaion()
