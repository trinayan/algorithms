import unittest
from ..data_structures.stack import Stack, EmptyStackError

class TestStack(unittest.TestCase):
    """
    Tests the methods of the Stack data structure.
    """

    def setUp(self):
        self.input = range(5)
        self.stack = Stack()
        self.reverse = [5, 4, 3, 2, 1]

    def test_stack(self):
        for i in self.input:
            self.stack.push(i)

        result = []

        while not self.stack.empty():
            result.append(self.stack.pop())

        self.assertEqual(self.reverse, result)
        self.assertRaises(EmptyStackError, self.stack.empty())
