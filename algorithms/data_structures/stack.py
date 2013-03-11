"""
Stacks are cool
"""

class EmptyStackError(Exception):
    pass

class Element(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, element):
        self.head = Element(element, self.head)

    def pop(self):
        if self.empty():
            raise EmptyStackError
        result = self.head.value
        self.head = self.head.next
        return result

    def empty(self):
        return self.head == None
