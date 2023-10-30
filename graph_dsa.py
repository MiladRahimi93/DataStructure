import graph_implementaion
import non_linear_dsa
import types_of_graph


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


def graph_definition():
    print(style.YELLOW + """
    In data structures, a graph is a non-linear data structure that consists of a set of vertices (also called nodes)
    and a set of edges that connect these vertices. A graph can be visualized as a collection of nodes, where each node
    represents a unique entity, and the edges represent the relationships or connections between these entities.

    Formally, a graph can be defined as G = (V, E), where V represents the set of vertices/nodes, and E represents the set
    of edges. The edges can be either directed or undirected, depending on whether the relationship between the vertices is
    one-way or bidirectional.

    Graphs are commonly used to represent various real-world scenarios, such as social networks, computer networks,
    transportation networks, and more. They provide a flexible and efficient way to model and analyze relationships
    between different entities.""")
    input(style.RED + "Enter any key to close: ")
    test()


# Terminalogy
def graph_terms():
    print(style.YELLOW + """
    [+] Graph terminology in data structures refers to the various terms and concepts used in the study and implementation
        of graphs. Some of the common terminology includes:

        1: Vertex: Also known as a node, it is a point on a graph where edges meet.
        2: Edge: A line or link connecting two vertices.
        3: Weight: A value assigned to an edge, representing the cost or distance between two vertices.
        4: Degree: The number of edges connected to a vertex.
        5: Path: A sequence of vertices connected by edges.
        6: Cycle: A path that starts and ends at the same vertex.
        7: Directed graph: A graph where edges have a direction.
        8: Undirected graph: A graph where edges have no direction.
        9: Adjacency matrix: A matrix representing the connections between vertices in a graph.
        10: Adjacency list: A list of vertices and their adjacent vertices in a graph.""")
    input(style.RED + "Enter any key to close: ")
    test()


# tree as nonlinear dsa
def why_non_linear_dsa_graph():
    print(style.YELLOW + """
    [+] Why graph is considered a non-linear data structure?
        The data in a graph are not stored in a sequential manner i.e., they are not stored linearly. Instead, they are arranged
        on multiple levels or we can say it is a hierarchical structure. For this reason, the graph is considered to be a
        non-linear data structure.""")
    input(style.RED + "Enter any key to close: ")
    test()


# properties of tree
def graph_properties():
    print(style.YELLOW + """
    [+]The properties of a data structure in a graph refer to the characteristics and behaviors that define how the graph
     is organized and accessed. Some common properties of data structures in graphs include:
        Representation: How the graph is represented in memory, such as using an adjacency matrix or adjacency list.        
        Vertex Storage: How the vertices/nodes of the graph are stored, including any associated data or attributes.        
        Edge Storage: How the edges/links between vertices are stored, including any associated data or attributes.        
        Traversal: The ability to visit and explore all vertices and edges in the graph, either through depth-first search
        (DFS) or breadth-first search (BFS).        
        Connectivity: The ability to determine if there is a path or connection between two vertices in the graph.       
        Weighted or Unweighted: Whether the graph has weighted edges, where each edge has a value or cost associated with
        it, or unweighted edges, where all edges have the same value.        
        Directed or Undirected: Whether the graph is directed, meaning the edges have a specific direction, or undirected,
        where edges have no specific direction.    
        Cycle Detection: The ability to detect if there is a cycle (a closed path) in the graph.        
        Operations: The operations that can be performed on the graph, such as adding or removing vertices or edges, 
        updating attributes, or finding the shortest path between two vertices.        
        These properties can vary depending on the specific implementation of the graph data structure.
    """)
    input(style.RED + "Enter any key to close: ")
    test()


# need for tree
def need_graph():
    print(style.YELLOW + """
    Graph data structures are essential for representing and solving various real-world problems that involve relationships
    or connections between entities. Here are some reasons why we need graph data structures:
        1: Modeling Relationships: Graphs are ideal for modeling relationships between entities. They can represent connections between
        people in social networks, web pages in a website, dependencies between tasks in a project, or connections between locations
        in a map.
        
        2: Network Analysis: Graphs are used extensively in network analysis to understand and analyze complex systems. They can
        represent communication networks, transportation networks, computer networks, or biological networks.
        
        3: Pathfinding and Routing: Graphs are efficient in finding paths and routes between two points. Algorithms like Dijkstra's
         algorithm and A* search algorithm can be used to find the shortest path or the most optimal route in a graph.
        
        4: Recommendation Systems: Graphs can be used to build recommendation systems by analyzing the connections between users, 
        products, or items. They can provide personalized recommendations based on the relationships and interactions within the graph.
        
        5: Social Network Analysis: Graphs are widely used in social network analysis to understand social structures, influence, 
        and patterns. They can help identify key influencers, communities, or clusters within a network.
        
        6: Data Integration: Graphs can be used to integrate data from various sources and represent complex relationships between different entities. They provide a flexible and scalable way to represent and query interconnected data.
        
        7: Visualization: Graphs can be visually represented to provide a clear and intuitive understanding of complex relationships. They can help in visualizing and analyzing data in fields like biology, social sciences, and computer networks.
        
        8: Overall, graph data structures provide a powerful and flexible way to represent, analyze, and solve problems that involve relationships and connections between entities.
    """)
    input(style.RED + "Enter any key to close: ")
    test()


# Application
def graph_application():
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
def advantage_of_graph():
    print(style.YELLOW + """
    Graphs have several advantages as a data structure, which include:
        
        Efficient Representation: Graphs are an efficient way to represent complex relationships between entities. They
         can represent
        connections between people in social networks, dependencies between tasks in a project, or connections between
         locations in a map.
        
        Flexibility: Graphs are a flexible data structure that can be used to represent a wide variety of relationships
        and connections. They can be used to model networks, relationships, and dependencies in various domains and industries.
        
        Easy to Traverse: Graphs are easy to traverse using algorithms like depth-first search or breadth-first search.
        These algorithms can be used to find paths, cycles, or connected components in a graph.
        
        Scalability: Graphs are scalable and can handle large amounts of data. They can be used to represent and analyze
        large networks, like social networks or the internet.
        
        Visualization: Graphs can be visually represented to provide a clear and intuitive understanding of complex
        relationships. They can help in visualizing and analyzing data in fields like biology, social sciences, and computer
        networks.
        
        Efficient Algorithms: There are several efficient algorithms that can be used to solve problems in graphs, like
        Dijkstra's algorithm, A* search algorithm, and minimum spanning tree algorithms. These algorithms can be used to
        find the shortest path, the most optimal route, or the minimum spanning tree in a graph.
        
        Recommendation Systems: Graphs can be used to build recommendation systems by analyzing the connections between
        users, products, or items. They can provide personalized recommendations based on the relationships and interactions
        within the graph.
        
        Overall, graphs provide a powerful and flexible way to represent, analyze, and solve problems that involve relationships
        and connections between entities. They enable efficient and effective solutions to problems in various domains and 
        industries.  """)
    input(style.RED + "Enter any key to close: ")
    test()


# disadvantage
def disadvantage_of_graph():
    print(style.YELLOW + """
    [+] While graphs have many advantages, they also come with some disadvantages. Here are a few:
        
        1: Storage Requirements: Graphs can require a significant amount of storage space compared to other data structures. Storing
        the connections between entities can consume more memory, especially for large graphs with numerous edges.
        
        2: Complexity: Graph algorithms can be complex and computationally expensive. Some graph problems, such as finding the shortest
        path in a weighted graph or determining the optimal solution in a large graph, can have high time complexity.
        
        3: Lack of Standardization: Unlike other data structures like arrays or linked lists, there is no standardized representation
        for graphs. Different graph implementations may have different features, making it challenging to interchange or share graph
        data between systems.
        
        4: Difficulty in Modification: Modifying a graph, particularly adding or removing edges or vertices, can be more complex and
        time-consuming compared to other data structures. Maintaining the integrity of the graph structure while making modifications
        requires careful handling.
        
        5: Traversal Complexity: In some cases, traversing a graph can be time-consuming, especially for large graphs with many vertices
        and edges. Algorithms like depth-first search or breadth-first search may take longer to complete, impacting the performance
        of graph-based applications.
        
        6: Lack of Global Information: When working with large graphs, it can be challenging to obtain a global view of the entire graph
        due to its size and complexity. Analyzing and extracting meaningful insights from the graph as a whole may require additional
        computational resources and specialized algorithms.
        
        7: Despite these disadvantages, graphs remain a powerful and widely used data structure for modeling and solving problems involving
        relationships and connections between entities. The choice of using a graph depends on the specific requirements and characteristics
        of the problem at hand.
    """)
    input(style.RED + "Enter any key to close: ")
    test()


def test():
    print(style.BLUE + """
    [+] Select an option form bellow:
        1: Definiation of Graph
        2: Basic Terminologies In graph Data Structure
        3: Types of graph data structures:
        4: Basic Operation Of graph Data Structure
        5: Why graph is considered a non-linear data structure?
        6: Properties of graph Data Structure:
        7: Need for graph Data Structure
        8: Application of graph Data Structure
        9: Advantages of graph Data Structure
        10: Disadvantages of graph Data Structure
        11: Back
        """)
    selection = input('Enter your selection: ')
    if selection == '1':
        graph_definition()
    elif selection == '2':
        graph_terms()
    elif selection == '3':
        types_of_graph.types_of_graph()
    elif selection == '4':
        graph_implementaion.graph_operations()
    elif selection == '5':
        why_non_linear_dsa_graph()
    elif selection == '6':
        graph_properties()
    elif selection == '7':
        need_graph()
    elif selection == '8':
        graph_application()
    elif selection == '9':
        advantage_of_graph()
    elif selection == '10':
        disadvantage_of_graph()
    elif selection == '11':
        non_linear_dsa.non_lineardsa_implementaion()
    else:
        print(style.RED + "Invalid input!!!")
        test()