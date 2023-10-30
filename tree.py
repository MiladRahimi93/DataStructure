import non_linear_dsa
import tree_types
import tree_implementation

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

def tree_definition():
    print(style.YELLOW + """
    A tree data structure is a hierarchical structure that is used to represent and organize data in a way that is easy
    to navigate and search. It is a collection of nodes that are connected by edges and has a hierarchical relationship
    between the nodes. 
    The topmost node of the tree is called the root, and the nodes below it are called the child nodes. Each node can
    have multiple child nodes, and these child nodes can also have their own child nodes, forming a recursive structure.
    """)
    input(style.RED + "Enter any key to close: ")
    test()
# Terminalogy
def tree_terms():
    print(style.YELLOW + """
    [+] Basic Terminologies In Tree Data Structure:
    1: Parent Node: The node which is a predecessor of a node is called the parent node of that node. {B} is the parent 
        node of {D, E}.
    2: Child Node: The node which is the immediate successor of a node is called the child node of that node. Examples: 
        {D, E} are the child nodes of {B}.
    3: Root Node: The topmost node of a tree or the node which does not have any parent node is called the root node.
     {A} is the root node of the tree. A non-empty tree must contain exactly one root node and exactly one path from 
     the root to all other nodes of the tree.
    4: Leaf Node or External Node: The nodes which do not have any child nodes are called leaf nodes. {K, L, M, N, O, P}
     are the leaf nodes of the tree.
    5: Ancestor of a Node: Any predecessor nodes on the path of the root to that node are called Ancestors of that node.
     {A,B} are the ancestor nodes of the node {E}
    6: Descendant: Any successor node on the path from the leaf node to that node. {E,I} are the descendants of the node
     {B}.
    7: Sibling: Children of the same parent node are called siblings. {D,E} are called siblings.
    8: Level of a node: The count of edges on the path from the root node to that node. The root node has level 0.
    9: Internal node: A node with at least one child is called Internal Node.
    10: Neighbour of a Node: Parent or child nodes of that node are called neighbors of that node.
    11: Subtree: Any node of the tree along with its descendant.""")
    input(style.RED + "Enter any key to close: ")
    test()
# tree as nonlinear dsa
def why_non_linear_dsa_tree():
    print(style.YELLOW + """
    [+] Why Tree is considered a non-linear data structure?
        The data in a tree are not stored in a sequential manner i.e., they are not stored linearly. Instead, they are arranged
        on multiple levels or we can say it is a hierarchical structure. For this reason, the tree is considered to be a
        non-linear data structure.""")
    input(style.RED + "Enter any key to close: ")
    test()
# properties of tree
def tree_properties():
    print(style.YELLOW + """
    [+]Properties of Tree Data Structure:
        1: Number of edges: An edge can be defined as the connection between two nodes. If a tree has N nodes then it will have
        2: (N-1) edges. There is only one path from each node to any other node of the tree.
        3: Depth of a node: The depth of a node is defined as the length of the path from the root to that node. Each edge
            adds 1 unit of length to the path. So, it can also be defined as the number of edges in the path from the root
            of the tree to the node.
        4: Height of a node: The height of a node can be defined as the length of the longest path from the node to a leaf
            node of the tree.
        5: Height of the Tree: The height of a tree is the length of the longest path from the root of the tree to a leaf
            node of the tree.
        6: Degree of a Node: The total count of subtrees attached to that node is called the degree of the node. The degree
            of a leaf node must be 0. The degree of a tree is the maximum degree of a node among all the nodes in the tree.
    """)
    input(style.RED + "Enter any key to close: ")
    test()

# need for tree
def need_tree():
    print(style.YELLOW + """
    [+] Need for Tree Data Structure
        1. One reason to use trees might be because you want to store information that naturally forms a hierarchy.
        2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays). 
        3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists). 
        4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on the number of nodes as nodes are
           linked using pointers.
    """)
    input(style.RED + "Enter any key to close: ")
    test()
# Application
def tree_application():
    print(style.YELLOW + """
    [+] Application of Tree Data Structure:
        File System:  This allows for efficient navigation and organization of files.
        Data Compression: Huffman coding is a popular technique for data compression that involves constructing a binary
        tree where the leaves represent characters and their frequency of occurrence. The resulting tree is used to encode
        the data in a way that minimizes the amount of storage required.
        
        Compiler Design: In compiler design, a syntax tree is used to represent the structure of a program. 
        Database Indexing: B-trees and other tree structures are used in database indexing to efficiently search for and
        retrieve data. 
    """)
    input(style.RED + "Enter any key to close: ")
    test()

# advantage of tree
def advantage_of_tree():
    print(style.YELLOW + """
    [+]Advantages of Tree Data Structure:
        Tree offer Efficient Searching Depending on the type of tree, with average search times of O(log n) for balanced
        treeslike AVL.
        Trees provide a hierarchical representation of data, making it easy to organize and navigate large
        amounts of information.
        The recursive nature of trees makes them easy to traverse and manipulate using recursive algorithms.
    """)
    input(style.RED + "Enter any key to close: ")
    test()
# disadvantage
def disadvantage_of_tree():
    print(style.YELLOW + """
    Disadvantages of Tree Data Structure:
    Unbalanced Trees, meaning that the height of the tree is skewed towards one side, which can lead to inefficient search times.
    Trees demand more memory space requirements than some other data structures like arrays and linked lists, especially
    if the tree is very large.
    The implementation and manipulation of trees can be complex and require a good understanding of the algorithms.""")
    input(style.RED + "Enter any key to close: ")
    test()



def test():
    print(style.BLUE + """
    [+] Select an option form bellow:
        1: Definiation of tree
        2: Basic Terminologies In Tree Data Structure
        3: Types of Tree data structures:
        4: Basic Operation Of Tree Data Structure
        5: Why Tree is considered a non-linear data structure?
        6: Properties of Tree Data Structure:
        7: Need for Tree Data Structure
        8: Application of Tree Data Structure
        9: Advantages of Tree Data Structure
        10: Disadvantages of Tree Data Structure
        11: Back
        """)
    selection = input('Enter your selection: ')
    if selection == '1':
        tree_definition()
    elif selection == '2':
        tree_terms()
    elif selection == '3':
        tree_types.types_of_tree()
    elif selection == '4':
        tree_implementation.tree_opreations()
    elif selection == '5':
        why_non_linear_dsa_tree()
    elif selection == '6':
        tree_properties()
    elif selection == '7':
        need_tree()
    elif selection == '8':
        tree_application()
    elif selection == '9':
        advantage_of_tree()
    elif selection == '10':
        disadvantage_of_tree()
    elif selection == '11':
        non_linear_dsa.non_lineardsa_implementaion()
    else:
        print(style.RED + "Invalid input!!!")
        test()