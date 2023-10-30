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

def tree_creating_implement():
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def insert_node(root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = insert_node(root.left, data)
        else:
            root.right = insert_node(root.right, data)
        return root

    def print_tree(root):
        if root:
            print_tree(root.left)
            print(root.data, end=' ')
            print_tree(root.right)
    try:
        size = int(input("Enter the size of the DSA tree: "))
        tree_root = None
    except:
        print(style.RED + "===Invalid input===")
        tree_creating_implement()
    for _ in range(size):
        try:
            node_data = int(input("Enter node value: "))
            tree_root = insert_node(tree_root, node_data)
        except:
            print(style.RED + "=====INVALID INPUT ENTER INT=====")
            tree_creating_implement()
    print(style.GREEN + "Tree:")
    print_tree(tree_root)
    input(style.RED + "\nEnter any key to back")
    tree_opreations()

def creation_binary_tree():
    print(style.GREEN + """
    [+] Select an option:
        1: code review
        2: implementaion
        3: Back
    """)
    selection = input("Enter your choice: ")
    if selection == '1':
        print(style.WHITE + """
        class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, data):
    if root is None:
        return Node(data)
    elif data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
    return root


def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data, end=' ')
        print_tree(root.right)


size = int(input("Enter the size of the DSA tree: "))
tree_root = None

for _ in range(size):
    node_data = int(input("Enter node value: "))
    tree_root = insert_node(tree_root, node_data)

print("Tree:")
print_tree(tree_root)
        
        
        """)
        input(style.RED + "Enter any key to close: ")
        creation_binary_tree()
    elif selection == '2':
        tree_creating_implement()
    elif selection == '3':
        tree_opreations()

def inserting_code_review():
    print(style.WHITE + """
        def insert_node(root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = insert_node(root.left, data)
        else:
            root.right = insert_node(root.right, data)
        return root
    """)
    input("Enter any key to back: ")
    inserting_in_tree()

def inserting_tree_Implementation():
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def insert_node(root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = insert_node(root.left, data)
        else:
            root.right = insert_node(root.right, data)
        return root

    def print_tree(root):
        if root:
            print_tree(root.left)
            print(root.data, end=' ')
            print_tree(root.right)

    try:
        size = int(input("Enter the size of the DSA tree: "))
        tree_root = None
    except:
        print(style.RED + "===Invalid input===")
        tree_creating_implement()
    for _ in range(size):
        try:
            node_data = int(input("Enter node value: "))
            tree_root = insert_node(tree_root, node_data)
        except:
            print(style.RED + "=====INVALID INPUT ENTER INT=====")
            tree_creating_implement()
    print(style.GREEN + "Tree:")
    print_tree(tree_root)
    try:
        print("\n")
        new_node_data = int(input("Enter new node value: "))
        tree_root = insert_node(tree_root, new_node_data)
    except:
        print(style.RED + "=====INVALID INPUT ENTER INT=====")
        tree_creating_implement()
    print(style.GREEN + "Tree after inserting is: ")
    print_tree(tree_root)
    print("")
    input(style.RED + "\nEnter any key to close: ")
    inserting_in_tree()

def inserting_in_tree():
    print(style.GREEN + """
    [+] Select an option:
        1: code review
        2: implementaion
        3: Back
    """)
    selection = input("Enter your choice: ")
    if selection == '1':
        inserting_code_review()
    elif selection == '2':
        inserting_tree_Implementation()
    elif selection == '3':
        tree_opreations()
    else:
        print(style.RED + "====INVALID INPUT====")
        inserting_in_tree()


# برسی موچودیت یک عنصر در تری یا درخت
# Python3 function to search a given key in a given BST

class Node:
	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to insert
# a new node with the given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the (unchanged) node pointer
	return node

# Utility function to search a key in a BST
def search(root, key):
	# Base Cases: root is null or key is present at root
	if root is None or root.key == key:
		return root

	# Key is greater than root's key
	if root.key < key:
		return search(root.right, key)

	# Key is smaller than root's key
	return search(root.left, key)

def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.key, end=" ")
        print_tree(node.right)
# Driver Code
def searching():
    try:
        root = None
        tree_root = eval(input("Enter the root of your tree node: "))
        root = insert(root, tree_root)
        tree_nodes = eval(input("Enter the numbers of your tree: "))
        for i in range(tree_nodes):
            element = eval(input("Enter the node valaue: "))
            insert(root, element)
        print("Your Created tree is as Bellow: ")
        print_tree(root)
        # Key to be found
        searching_element = eval(input("\nEnter the node for searching: "))



        # Searching in a BST
        if search(root, searching_element) is None:
            print(searching_element, "not found")
        else:
            print(searching_element, "found")
        input(style.RED +  "Enter a key to back.")
        searching_process()
    except:
        input("++++INVALID INPUT ENTER A INT++++")
        searching()

def searching_process():
    print(style.YELLOW +  """
    [+] Select an option:
        1: code review
        2: Implementaion
        3: Back
    """)
    selection = input("Enter your choice:")
    if selection == '1':
        print(style.WHITE + """
def searching():
    try:
        root = None
        tree_root = eval(input("Enter the root of your tree node: "))
        root = insert(root, tree_root)
        tree_nodes = eval(input("Enter the numbers of your tree: "))
        for i in range(tree_nodes):
            element = eval(input("Enter the node valaue: "))
            insert(root, element)
        print("Your Created tree is as Bellow: ")
        print_tree(root)
        # Key to be found
        searching_element = eval(input("\nEnter the node for searching: "))
        


        # Searching in a BST
        if search(root, searching_element) is None:
            print(searching_element, "not found")
        else:
            print(searching_element, "found")
        input(style.RED +  "Enter a key to back.")
    except:
        input("++++INVALID INPUT ENTER A INT++++")
        searching()

        """)
        input(style.RED + "Enter a Key to close: ")
        searching_process()
    elif selection == '2':
        searching()
    elif selection == '3':
        tree_opreations()
    else:
        print(style.RED + "INVALID INPUT TRY AGAIN!!!")
        searching_process()



def depth_of_node():
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def insert(root, val):
        if root is None:
            return Node(val)
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root

    def find_depth(root, val, depth=0):
        if root is None:
            return None
        if root.val == val:
            return depth
        left_depth = find_depth(root.left, val, depth + 1)
        if left_depth is not None:
            return left_depth
        right_depth = find_depth(root.right, val, depth + 1)
        if right_depth is not None:
            return right_depth
        return None

    # Create a tree
    try:
        root = None
        tree_root = int(input("Enter the root of your tree: "))
        root = insert(root, tree_root)
        tree_nodes = int(input("Enter the number of nodes in your tree: "))
        for i in range(tree_nodes):
            element = int(input("Enter the node value: "))
            insert(root, element)

        # Get user input for node
        node = int(input("Enter the node for which you want to find the depth: "))

        # Find the depth of the node
        depth = find_depth(root, node)
        if depth is None:
            print("Node not found")
        else:
            print("Depth of node", node, "is", depth)
            depth_process()
    except:
        print(style.RED + "Invalid input!!!")
        depth_of_node()


def depth_process():
    print(style.YELLOW + """
    [+] Select an option: 
        1: implementaion
        2: code review
        3: Back
    """)
    select = input("Enter an option: ")
    if select == '1':
        depth_of_node()
    elif select == '2':
        print(style.WHITE + """
        
def depth_of_node():
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def insert(root, val):
        if root is None:
            return Node(val)
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root

    def find_depth(root, val, depth=0):
        if root is None:
            return None
        if root.val == val:
            return depth
        left_depth = find_depth(root.left, val, depth + 1)
        if left_depth is not None:
            return left_depth
        right_depth = find_depth(root.right, val, depth + 1)
        if right_depth is not None:
            return right_depth
        return None

    # Create a tree
    try:
        root = None
        tree_root = int(input("Enter the root of your tree: "))
        root = insert(root, tree_root)
        tree_nodes = int(input("Enter the number of nodes in your tree: "))
        for i in range(tree_nodes):
            element = int(input("Enter the node value: "))
            insert(root, element)
    
        # Get user input for node
        node = int(input("Enter the node for which you want to find the depth: "))
    
        # Find the depth of the node
        depth = find_depth(root, node)
        if depth is None:
            print("Node not found")
        else:
            print("Depth of node", node, "is", depth)
            depth_process()
    except:
        print(style.RED + "Invalid input!!!")
        depth_of_node()

        """)
        input("Enter a key to close: ")
        depth_process()
    elif select == '3':
        tree_opreations()
    else:
        input(style.RED + "INVALID INPUT TRY AGAIN: ")
        depth_process()
# ترویرسیر یک تری

def traversing_tree():
    print(style.YELLOW + """
    [+] Select an option:
        1: Depth First search
        2: Breath first search
        3: Boundry traversal
        4: Diagonal Traversal
        5: Back
    """)
    selection = input("Enter your choice: ")
    if selection == '1':
        print("""
        [+] Select an option:
            1: Inorder traversal
            2: preorder traversal
            3: post order traversal
            4: back
        """)
        dpt_selection = input("Enter youe choice:")
        if dpt_selection == '1':
            print("""
        [+] Select an option:
            1: Algorithm
            2: Image
            3: code review
            4: back    
            """)
            option_selection = input("Enter your choice: ")
            if option_selection == '1':
                print("""
            [+]Algorithm Inorder(tree)
                1: Traverse the left subtree, i.e., call Inorder(left->subtree)
                2: Visit the root.
                3: Traverse the right subtree, i.e., call Inorder(right->subtree)
                """)
                input("Enter your a key to back")
                traversing_tree()
            elif option_selection == '2':
                img = cv2.imread('traversal.png', cv2.IMREAD_GRAYSCALE)
                dim = (450, 350)
                resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                cv2.imshow('image', resized)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                traversing_tree()
            elif option_selection == '3':
                print(style.WHITE + """
# Python3 program to for tree traversals
 
 
# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # Then print the data of node
        print(root.val, end=" "),
 
        # Now recur on right child
        printInorder(root.right)
 
 
# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("Inorder traversal of binary tree is")
    printInorder(root)
                """)
                input("Enter a key to close: ")
                traversing_tree()
            elif option_selection == '4':
                traversing_tree()
            else:
                print(style.RED + """Invalid input""")
                traversing_tree()
        elif dpt_selection == '2':
            print("""
        [+] Select an option:
            1: Algorithm
            2: Image
            3: code review
            4: back    
            """)
            option_selection = input("Enter your choice: ")
            if option_selection == '1':
                print("""
            [+]Algorithm Preorder(tree)
                1: Visit the root.
                2: Traverse the left subtree, i.e., call Preorder(left->subtree)
                3: Traverse the right subtree, i.e., call Preorder(right->subtree) 
                """)
                input("Enter your a key to back")
                traversing_tree()
            elif option_selection == '2':
                img = cv2.imread('traversal.png', cv2.IMREAD_GRAYSCALE)
                dim = (450, 350)
                resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                cv2.imshow('image', resized)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                traversing_tree()
            elif option_selection == '3':
                print(style.WHITE + """class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do preorder tree traversal
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val, end=" "),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)
 
 
                """)
                input("Enter a key to close: ")
                traversing_tree()
            elif option_selection == '4':
                traversing_tree()
            else:
                print(style.RED + """Invalid input""")
                traversing_tree()
        elif dpt_selection == '3':
            print("""
        [+] Select an option:
            1: Algorithm
            2: Image
            3: code review
            4: back    
            """)
            option_selection = input("Enter your choice: ")
            if option_selection == '1':
                print("""
                [+]Algorithm Postorder(tree)
                    1: Traverse the left subtree, i.e., call Postorder(left->subtree)
                    2: Traverse the right subtree, i.e., call Postorder(right->subtree)
                    3: Visit the root
                """)
                input("Enter your a key to back")
                traversing_tree()
            elif option_selection == '2':
                img = cv2.imread('traversal.png', cv2.IMREAD_GRAYSCALE)
                dim = (450, 350)
                resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                cv2.imshow('image', resized)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                traversing_tree()
            elif option_selection == '3':
                print(style.WHITE + """
                class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # The recur on right child
        printPostorder(root.right)
 
        # Now print the data of node
        print(root.val, end=" "),
 
 
                """)
                input("Enter a key to close: ")
                traversing_tree()
            elif option_selection == '4':
                traversing_tree()
            else:
                print(style.RED + """Invalid input""")
                traversing_tree()
        elif dpt_selection == '4':
            traversing_tree()
        else:
            print(style.RED + "Invalid input")
            traversing_tree()
    elif selection == '2':
        print(style.YELLOW + """
        [+] Enter a selection:
            1: Defination
            2: Code review
            3: Image
            4: Back
        """)
        selecting_option = input("Enter an option: ")
        if selecting_option == '1':
            print("""
            [+]Breath First Searching
            Level Order Traversal technique is defined as a method to traverse a Tree such that all nodes present in the
            same level are traversed completely before traversing the next level.
            How does Level Order Traversal work?
            The main idea of level order traversal is to traverse all the nodes of a lower level before moving to any of
            the nodes of a higher level. This can be done in any of the following ways: 
            the naive one (finding the height of the tree and traversing each level and printing the nodes of that level)
            efficiently using a queue.
            """)
            input(style.RED + "Enter a key to close:")
            traversing_tree()
        elif selecting_option == '2':
            print(style.WHITE + """
# Recursive Python program for level
# order traversal of Binary Tree


# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


# Function to print level order traversal of tree
def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printCurrentLevel(root, i)


# Print nodes at a current level
def printCurrentLevel(root, level):
	if root is None:
		return
	if level == 1:
		print(root.data, end=" ")
	elif level > 1:
		printCurrentLevel(root.left, level-1)
		printCurrentLevel(root.right, level-1)


# Compute the height of a tree--the number of nodes
# along the longest path from the root node down to
# the farthest leaf node
def height(node):
	if node is None:
		return 0
	else:

		# Compute the height of each subtree
		lheight = height(node.left)
		rheight = height(node.right)

		# Use the larger one
		if lheight > rheight:
			return lheight+1
		else:
			return rheight+1


# Driver program to test above function
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print("Level order traversal of binary tree is -")
	printLevelOrder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

            """)
            input("Enter a key to close: ")
            traversing_tree()
        elif selecting_option == '3':
            img = cv2.imread('breath.jpg', cv2.IMREAD_GRAYSCALE)
            dim = (450, 350)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow('image', resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            traversing_tree()
        elif selecting_option == '4':
            traversing_tree()
        else:
            input(style.RED + "Invalid input try again.")
            traversing_tree()
    elif selection == '3':
        print(style.YELLOW + """
        [+] Enter a selection:
            1: Defination
            2: Code review
            3: Image
            4: Back
        """)
        selecting_option = input("Enter an option: ")
        if selecting_option == '1':
            print("""
Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.

 The boundary includes 

left boundary (nodes on left excluding leaf nodes)
leaves (consist of only the leaf nodes)
right boundary (nodes on right excluding leaf nodes)
The left boundary is defined as the path from the root to the left-most node. The right boundary is defined as the path from the root to the right-most node. If the root doesn’t have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not apply to any subtrees.
The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if it exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
The right-most node is also defined in the same way with left and right exchanged. 
For example, boundary traversal of the following tree is “20 8 4 10 14 25 22”

This is how we write the traversal:

root : 20

left- boundary nodes: 8

leaf nodes: 4 10 14 25

right – boundary nodes: 22 
            """)
            input(style.RED + "Enter a key to close:")
            traversing_tree()
        elif selecting_option == '2':
            print(style.WHITE + """# Python3 program for binary traversal of binary tree

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None

# A simple function to print leaf nodes of a Binary Tree
def printLeaves(root):
	if(root):
		printLeaves(root.left)
		
		# Print it if it is a leaf node
		if root.left is None and root.right is None:
			print(root.data),

		printLeaves(root.right)

# A function to print all left boundary nodes, except a 
# leaf node. Print the nodes in TOP DOWN manner
def printBoundaryLeft(root):
	
	if(root):
		if (root.left):
			
			# to ensure top down order, print the node
			# before calling itself for left subtree
			print(root.data)
			printBoundaryLeft(root.left)
		
		elif(root.right):
			print (root.data)
			printBoundaryLeft(root.right)
		
		# do nothing if it is a leaf node, this way we
		# avoid duplicates in output


# A function to print all right boundary nodes, except
# a leaf node. Print the nodes in BOTTOM UP manner
def printBoundaryRight(root):
	
	if(root):
		if (root.right):
			# to ensure bottom up order, first call for
			# right subtree, then print this node
			printBoundaryRight(root.right)
			print(root.data)
		
		elif(root.left):
			printBoundaryRight(root.left)
			print(root.data)

		# do nothing if it is a leaf node, this way we 
		# avoid duplicates in output


# A function to do boundary traversal of a given binary tree
def printBoundary(root):
	if (root):
		print(root.data)
		
		# Print the left boundary in top-down manner
		printBoundaryLeft(root.left)

		# Print all leaf nodes
		printLeaves(root.left)
		printLeaves(root.right)

		# Print the right boundary in bottom-up manner
		printBoundaryRight(root.right)


# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printBoundary(root)

# This code is contributed by 
# Nikhil Kumar Singh(nickzuck_007)

            """)
            input("Enter a key to close: ")
            traversing_tree()
        elif selecting_option == '3':
            img = cv2.imread('boundry.png', cv2.IMREAD_GRAYSCALE)
            dim = (450, 350)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow('image', resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            traversing_tree()
        elif selecting_option == '4':
            traversing_tree()
        else:
            input(style.RED + "Invalid input try again.")
            traversing_tree()
    elif selection == '4':
        print(style.YELLOW + """
        [+] Enter a selection:
            1: Defination
            2: Code review
            3: Image
            4: Back
        """)
        selecting_option = input("Enter an option: ")
        if selecting_option == '1':
            print("""
Diagonal traversal refers to a method of traversing or visiting elements in a matrix or a 
two-dimensional array in a diagonal pattern. In this traversal, the elements are accessed diagonally, starting from the
top-left corner and moving towards the bottom-right corner or vice versa.

In a matrix, the diagonal elements are those elements that have the same row and column index, such as (0,0), (1,1),
(2,2), and so on. Diagonal traversal involves visiting these elements in a specific order.

There are two common approaches for diagonal traversal:

Top-Down Approach: In this approach, the traversal starts from the top-left corner and moves diagonally downwards until
 it reaches the bottom-right corner. Each diagonal is traversed from the top to the bottom, visiting the elements in that
  diagonal.

Bottom-Up Approach: In this approach, the traversal starts from the bottom-left corner and moves diagonally upwards until
 it reaches the top-right corner. Each diagonal is traversed from the bottom to the top, visiting the elements in that 
 diagonal.

Diagonal traversal can be useful in various scenarios, such as matrix manipulation, image processing, and data analysis.
 It allows for efficient access to elements in a diagonal pattern, which can be helpful in solving specific problems or extracting relevant information from the matrix.
            """)
            input(style.RED + "Enter a key to close:")
            traversing_tree()
        elif selecting_option == '2':
            print(style.WHITE + """
            # Python program for diagonal 
# traversal of Binary Tree

# A binary tree node
class Node:

	# Constructor to create a 
	# new binary tree node
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None
					d+1, diagonalPrintMap)
	
	# Vertical distance remains 
	# same for right child
	diagonalPrintUtil(root.right, 
						d, diagonalPrintMap)



# Print diagonal traversal of given binary tree
def diagonalPrint(root):

	# Create a dict to store diagonal elements 
	diagonalPrintMap = dict()
	
	# Find the diagonal traversal
	diagonalPrintUtil(root, 0, diagonalPrintMap)

	print ("Diagonal Traversal of binary tree : ")
	for i in diagonalPrintMap:
		for j in diagonalPrintMap[i]:
			print (j,end=" ")
		print()


# Driver Program 
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

diagonalPrint(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

            """)
            input("Enter a key to close: ")
            traversing_tree()
        elif selecting_option == '3':
            img = cv2.imread('diagonal.png', cv2.IMREAD_GRAYSCALE)
            dim = (450, 350)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow('image', resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            traversing_tree()
        elif selecting_option == '4':
            traversing_tree()
        else:
            input(style.RED + "Invalid input try again.")
            traversing_tree()
    elif selection == '5':
        tree_opreations()
    else:
        print(style.RED + "+++INVALID INPUT TRY AGAIN+++")
        traversing_tree()

def tree_opreations():
    print(style.GREEN + """
    [+] Types of opreations on tree:
    The tree is a hierarchical Data Structure. A binary tree is a tree that has at most two children. The node which is
    on the left of the Binary Tree is called “Left-Child” and the node which is the right is called “Right-Child”. Also,
    the smaller tree or the subtree in the left of the root node is called the “Left sub-tree” and that is on the right 
    is called “Right sub-tree”.
        1: Creation of binary tree
        2: insert
        3: searching
        4: traversing
        5: Depth calculation
        6: Back
    """)
    type_selection = input("Enter Yuor choice: ")
    if type_selection == '1':
        creation_binary_tree()
    elif type_selection == '2':
        inserting_in_tree()
    elif type_selection == '3':
        searching()
    elif type_selection == '4':
        traversing_tree()
    elif type_selection == '5':
        depth_process()
    elif type_selection == '6':
        tree.test()
    else:
        input(style.RED + "++++INVALID INPUT++++")
        tree_opreations()


