"""
Stack module will go here
"""

class EmptyStackException(Exception):
    pass

class Element(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack(object):
    def __init__(self):
        self.head = None

    def push(self):
        pass

    def pop(self):
        pass

    def empty(self):
        pass
