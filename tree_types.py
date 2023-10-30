import cv2
import tree
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
def general_tree():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
    If no constraint is placed on the tree’s hierarchy, a tree is called a general tree. Every node may have infinite
    numbers of children in General Tree. The tree is the super-set of all other trees.
        """)
        input("Enter a key to close: ")
        general_tree()
    elif selector == '2':
        img = cv2.imread('generaltree.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        general_tree()
    elif selector == '3':
        types_of_tree()
    else:
        print(style.RED + "Invalid input!!!")
        general_tree()

# Binary tree
def binary_tree():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        [+] Binary Tree
            The binary tree is the kind of tree in which most two children can be found for each parent. The kids are known as the
            left kid and right kid. This is more popular than most other trees. When certain constraints and characteristics
            are applied in a Binary tree, a number of others such as AVL tree, BST (Binary Search Tree), RBT tree, etc. are also
            used. When we move forward, we will explain all these styles in detail.
        """)
        input("Enter a key to close: ")
        general_tree()
    elif selector == '2':
        img = cv2.imread('generaltree.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        binary_tree()
    elif selector == '3':
        types_of_tree()
    else:
        print(style.RED + "Invalid input!!!")
        binary_tree()
# Binary search tree
def BST():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        [+] Binary Search Tree
            Binary Search Tree (BST) is a binary tree extension with several optional restrictions. The left child value
            of a node should in BST be less than or equal to the parent value, and the right child value should always be
            greater than or equal to the parent’s value. This Binary Search Tree property makes it ideal for search
            operations since we can accurately determine at each node whether the value is in the left or right sub-tree.
            This is why the Search Tree is named. """)
        input("Enter a key to close: ")
        general_tree()
    elif selector == '2':
        img = cv2.imread('bst.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        BST()
    elif selector == '3':
        types_of_tree()
    else:
        print(style.RED + "Invalid input!!!")
        BST()

# AVL Tree
def avl_tree():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        AVL tree is a binary search tree self-balancing. On behalf of the inventors Adelson-Velshi and Landis,
        the name AVL is given. This was the first tree that balanced dynamically. A balancing factor is allocated for
        each node in the AVL tree, based on whether the tree is balanced or not. The height of the node kids is at most 1.
        AVL vine. In the AVL tree, the correct balance factor is 1, 0 and -1. If the tree has a new node, it will be rotated
        to ensure that it is balanced. It will then be rotated. Common operations such as viewing, insertion, and removal
        take O(log n) time in the AVL tree. It is mostly applied when working with Lookups operations. """)
        input("Enter a key to close: ")
        avl_tree()
    elif selector == '2':
        img = cv2.imread('avl.webp', cv2.IMREAD_GRAYSCALE)
        cv2.imshow('image', img)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        avl_tree()
    elif selector == '3':
        types_of_tree()
    else:
        print(style.RED + "Invalid input!!!")
        avl_tree()

# Red Back Tree
def red_black_tree():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        [+] Red-Black Tree
            Another kind of auto-balancing tree is red-black. According to the red-black tree’s properties, the red-black 
            name is given
            because the Red-black tree has either red or Black painted on each node. It maintains the balance of the forest.
            Even though this tree is not fully balanced, the searching operation only takes O (log n) time. When the new
            nodes are added in Red-Black Tree, nodes will be rotated to maintain the Red-Black Tree’s properties. """)
        input("Enter a key to close: ")
        red_black_tree()
    elif selector == '2':
        img = cv2.imread('rbtree.png', cv2.IMREAD_GRAYSCALE)

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        red_black_tree()
    elif selector == '3':
        types_of_tree()
    else:
        print(style.RED + "Invalid input!!!")
        red_black_tree()

# N-ary tree
def n_ary_tree():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        [+] N-ary Tree
            The maximum number of children in this type of tree with a node is N. A binary tree is a two-year tree, as at
            most 2 children in every binary tree node. A complete N-ary tree is a tree where kids of a node either are
            0 or N. """)
        input("Enter a key to close: ")
        n_ary_tree()
    elif selector == '2':
        img = cv2.imread('narytree.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        n_ary_tree()
    elif selector == '3':
        types_of_tree()
    else:
        print(style.RED + "Invalid input!!!")
        n_ary_tree()





def types_of_tree():
    print(style.GREEN + """
    [+] Types of tree is as bellow:
        1: General Tree
        2: Binary Tree
        3: Binary search tree BST
        4: AVL Tree
        5: Red-Black Tree
        6: N-ary Tree
        7: Back
    """)
    tree_types_selection = input('Enter your selection: ')
    if tree_types_selection == '1':
        general_tree()
    elif tree_types_selection =='2':
        binary_tree()
    elif tree_types_selection =='3':
        BST()
    elif tree_types_selection == '4':
        avl_tree()
    elif tree_types_selection == '5':
        red_black_tree()
    elif tree_types_selection == '6':
        n_ary_tree()
    elif tree_types_selection == '7':
        tree.test()
    else:
        print(style.RED + "++Invalid input++")
        types_of_tree()
