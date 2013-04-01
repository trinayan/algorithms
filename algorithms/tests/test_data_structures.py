""" Unit Tests for data structures """
import unittest
from ..data_structures import undirected_adjacency_matrix


class TestUndirectedAdjacencyMatrix(unittest.TestCase):
    """
    Tests edge cases for Undirected Adjacency Matrix
    """

    def setUp(self):
        self.graph = undirected_adjacency_matrix.UndirectedAdjacencyMatrix()
        self.expected = []

        #Test empty graph
        self.expected.append({})

        #Test adding vertices
        self.expected.append({v: {i: float('inf') for i in range(20)}
                                 for v in range(20)})

        #Test removing vertices
        self.expected.append({v: {i: float('inf') for i in range(0, 20, 2)}
                                 for v in range(0, 20, 2)})

        #Test adding edges
        self.expected.append({v: {i: 1 for i in range(0, 20, 2)}
                                 for v in range(0, 20, 2)})

        #Test removing edges
        self.expected.append({v: {i: 1 if (i < 10 and v < 10) or
                                     (i >= 10 and v >= 10) else float('inf')
                                     for i in range(0, 20, 2)}
                                 for v in range(0, 20, 2)})

        #Test empty graph after removing all vertices
        self.expected.append({})

    def test_undirected_adjacency_matrix(self):
        #Test empty graph
        self.assertEqual(self.expected[0], self.graph.edge)

        #Test adding vertices
        #Should result in 20 vertices with no edges
        for i in range(20):
            self.graph.addVertex(i)
        self.assertEqual(self.expected[1], self.graph.edge)

        #Test removing vertices
        #Should result in 10 even-numbered vertices with no edges
        for i in range(1, 20, 2):
            self.graph.removeVertex(i)
        self.assertEqual(self.expected[2], self.graph.edge)

        #Test adding edges
        #Should result in a complete graph
        for i in range(0, 20, 2):
            for j in range(0, 20, 2):
                self.graph.addEdge(i, j)
        self.assertEqual(self.expected[3], self.graph.edge)

        #Test removing edges
        #Should result in two complete components: vertices 0-8, 10-18
        for i in range(0, 10, 2):
            for j in range(10, 20, 2):
                self.graph.removeEdge(i ,j)
        for i in range(10, 20, 2):
            for j in range(0, 10, 2):
                self.graph.removeEdge(i, j)
        self.assertEqual(self.expected[4], self.graph.edge)

        #Test empty graph after removing all vertices
        for i in range(0, 20, 2):
            self.graph.removeVertex(i)
        self.assertEqual(self.expected[5], self.graph.edge)
