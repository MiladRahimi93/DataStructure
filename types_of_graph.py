import cv2
import graph_dsa
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

def undirected_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Undirected Graphs: A graph in which edges have no direction, i.e., the edges do not have arrows indicating the
        direction of traversal. Example: A social network graph where friendships are not directional.
        """)
        input("Enter a key to close: ")
        undirected_graph()
    elif selector == '2':
        img = cv2.imread('graphdirect.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        undirected_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        undirected_graph()

def directed_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Directed Graphs: A graph in which edges have a direction, i.e., the edges have arrows indicating the direction of
        traversal. Example: A web page graph where links between pages are directional.
        """)
        input("Enter a key to close: ")
        directed_graph()
    elif selector == '2':
        img = cv2.imread('graphdirect.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        directed_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        directed_graph()

def wieghted_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Weighted Graphs: A graph in which edges have weights or costs associated with them. Example: A road network graph
        where the weights can represent the distance between two cities.
        """)
        input("Enter a key to close: ")
        wieghted_graph()
    elif selector == '2':
        img = cv2.imread('wgraph.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        wieghted_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        wieghted_graph()

def unwieghted_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Unweighted Graphs: A graph in which edges have no weights or costs associated with them. Example: A social network
        graph where the edges represent friendships.
        """)
        input("Enter a key to close: ")
        unwieghted_graph()
    elif selector == '2':
        img = cv2.imread('unwieghtedgraph.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        unwieghted_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        unwieghted_graph()

def complete_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Complete Graphs: A graph in which each vertex is connected to every other vertex. Example: A tournament graph
        where every player plays against every other player.
        """)
        input("Enter a key to close: ")
        complete_graph()
    elif selector == '2':
        img = cv2.imread('cgraph.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        complete_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        complete_graph()

def bipartite_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Bipartite Graphs: A graph in which the vertices can be divided into two disjoint sets such that every edge connects
        a vertex in one set to a vertex in the other set. Example: A job applicant graph where the vertices can be divided
        into job applicants and job openings.
        """)
        input("Enter a key to close: ")
        bipartite_graph()
    elif selector == '2':
        img = cv2.imread('bipartite.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        bipartite_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        bipartite_graph()

def tree_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Trees: A connected graph with no cycles. Example: A family tree where each person is connected to their parents.
        """)
        input("Enter a key to close: ")
        tree_graph()
    elif selector == '2':
        img = cv2.imread('treegraph.jpg', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        tree_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        tree_graph()

def cycle_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Cycles: A graph with at least one cycle. Example: A bike-sharing graph where the cycles represent the routes
        that the bikes take.
         """)
        input("Enter a key to close: ")
        cycle_graph()
    elif selector == '2':
        img = cv2.imread('cycle.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cycle_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        cycle_graph()

def sparse_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Sparse Graphs: A graph with relatively few edges compared to the number of vertices. Example: A chemical reaction
        graph where each vertex represents a chemical compound and each edge represents a reaction between two compounds.
         """)
        input("Enter a key to close: ")
        sparse_graph()
    elif selector == '2':
        img = cv2.imread('sparse.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        sparse_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        sparse_graph()

def dense_graph():
    print(style.YELLOW + """
    [+] Select an option:
        1: Definition
        2: Image
        3: back
    """)
    selector = input("Enter your choice: ")
    if selector == "1":
        print("""
        Dense Graphs: A graph with many edges compared to the number of vertices. Example: A social network graph where
        each vertex represents a person and each edge represents a friendship.
        """)
        input("Enter a key to close: ")
        dense_graph()
    elif selector == '2':
        img = cv2.imread('sparse.png', cv2.IMREAD_GRAYSCALE)
        dim = (450,350)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        dense_graph()
    elif selector == '3':
        types_of_graph()
    else:
        print(style.RED + "Invalid input!!!")
        dense_graph()

def types_of_graph():
    print(style.GREEN + """
    [+] Types of graph is as bellow:
        0: general tree
        1: Undirected graph
        2: Directed Graph
        3: Wieghted graph
        4: Unwieghted graph
        5: complete graph
        6: Bipartite graph
        7: Trees
        8: Cycles
        9: Sparse Graph
        10: Dense Graph
        11: Back
    """)
    graph_types_selection = input('Enter your selection: ')
    if graph_types_selection == '0':
        general_tree()
    elif graph_types_selection == '1':
        undirected_graph()
    elif graph_types_selection == '2':
        directed_graph()
    elif graph_types_selection == '3':
        wieghted_graph()
    elif graph_types_selection == '4':
        unwieghted_graph()
    elif graph_types_selection == '5':
        complete_graph()
    elif graph_types_selection == '6':
        bipartite_graph()
    elif graph_types_selection == '7':
        tree_graph()
    elif graph_types_selection == '8':
        cycle_graph()
    elif graph_types_selection == '9':
        sparse_graph()
    elif graph_types_selection == '10':
        dense_graph()
    elif graph_types_selection == '11':
        graph_dsa.test()
    else:
        print(style.RED + "+++INVALID INPUT+++")
        types_of_graph()

