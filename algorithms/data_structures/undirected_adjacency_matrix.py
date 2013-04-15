"""
    undirected_adjacency_matrix.py

    Implementation of a graph as an undirected adjacency matrix.

    Undirected Adjacency Matrix Overview:
    --------------------------------------
    Edges are stored as a two-dimensional matrix of weights.
    Vertices are represented as the rows and columns of the matrix.
    Since the graph is undirected, for any two vertices x and y:
        edge(x,y) == edge(y,x)


    Time complexity:
    ----------------
    V = Number of vertices

    Storage:       O(V**2)
    Add vertex:    O(V**2)
    Add edge:      O(1)
    Remove vertex: O(v**2)
    Remove edge:   O(1)
    Query:         O(1)

    Graph comparison: http://en.wikipedia.org/wiki/Graph_(abstract_data_type)
    Wiki: http://en.wikipedia.org/wiki/Adjacency_matrix

"""


class UndirectedAdjacencyMatrix:
    def __init__(self):
        self.edge = {}
        self.numVertices = 0

    def addVertex(self, key):
        if key in self.edge:
            return
        self.edge[key] = {v: float('inf') for v in self.edge}
        for i in self.edge:
            self.edge[i][key] = float('inf')
        self.numVertices += 1

    def removeVertex(self, key):
        if key not in self.edge:
            return
        del self.edge[key]
        for i in self.edge:
            del self.edge[i][key]
        self.numVertices -= 1

    def addEdge(self, x, y, weight = 1):
        if all (v in self.edge for v in (x, y)):
            self.edge[x][y] = self.edge[y][x] = weight

    def removeEdge(self, x, y):
        if all (v in self.edge for v in (x, y)):
            self.edge[x][y] = self.edge[y][x] = float('inf')
