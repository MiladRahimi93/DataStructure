import graph_dsa


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
            self.edges.append((vertex1, vertex2))
        else:
            print("One or both vertices do not exist!")

    def search_vertex(self, vertex):
        return vertex in self.vertices

    def traverse_graph(self):
        for vertex, adjacent_vertices in self.vertices.items():
            print(vertex, "->", adjacent_vertices)

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_edges(self):
        return self.edges


def create_graph():
    graph = Graph()
    num_vertices = int(input("Enter the number of vertices: "))
    for i in range(num_vertices):
        vertex = input("Enter vertex {}: ".format(i+1))
        graph.add_vertex(vertex)
    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        vertex1 = input("Enter vertex 1 of edge {}: ".format(i+1))
        vertex2 = input("Enter vertex 2 of edge {}: ".format(i+1))
        graph.add_edge(vertex1, vertex2)
    print("Graph created successfully!")
    return graph


def insert_into_graph(graph):
    vertex = input("Enter the vertex to add: ")
    graph.add_vertex(vertex)
    print("Vertex added successfully!")


def search_in_graph(graph):
    vertex = input("Enter the vertex to search: ")
    if graph.search_vertex(vertex):
        print("Vertex found in the graph!")
    else:
        print("Vertex not found in the graph!")


def traverse_graph(graph):
    graph.traverse_graph()


def display_vertices(graph):
    print("Vertices:", graph.get_vertices())


def display_edges(graph):
    print("Edges:", graph.get_edges())


def graph_operations():
    print("""
    [+] Types of operations on Graph:
        1: Create graph
        2: Insert into graph
        3: Search in graph
        4: Traverse graph
        5: Display vertices
        6: Display edges
        7: Exit
    """)
    graph = None
    while True:
        type_selection = input("Enter your choice: ")
        if type_selection == '1':
            graph = create_graph()
        elif type_selection == '2':
            if graph:
                insert_into_graph(graph)
            else:
                print("Please create a graph first!")
        elif type_selection == '3':
            if graph:
                search_in_graph(graph)
            else:
                print("Please create a graph first!")
        elif type_selection == '4':
            if graph:
                traverse_graph(graph)
            else:
                print("Please create a graph first!")
        elif type_selection == '5':
            if graph:
                display_vertices(graph)
            else:
                print("Please create a graph first!")
        elif type_selection == '6':
            if graph:
                display_edges(graph)
            else:
                print("Please create a graph first!")
        elif type_selection == '7':
            break
        else:
            print("Invalid input")

        if graph:
            print("Current Graph:")
            graph.traverse_graph()
    graph_dsa.test()