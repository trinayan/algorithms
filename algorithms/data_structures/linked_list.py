"""
    linked_list.py

    A basic linked list implementation.

    Linked List Overview:
    ----------------------
    Data is stored in an 'Element' or 'Node'.
    An element also contains a reference (link) to the next element in
    the list, hence the name 'linked list'.
    The main benefit of a linked list is that elements can be inserted
    or removed very quickly, as these operations only require modifying
    a reference. The main drawback is that there is no random access, so
    accessing a particular element requires traversing the list from
    the beginning.

    Many augmented forms of linked lists exist, but this particular
    implementation is the most basic (singly linked list).


    Time complexity:
    ----------------
    Indexing:                   O(n)
    Insert/delete at beginning: O(1)
    Insert/delete at end:       O(1) if tail reference is kept, O(n) otherwise
    Insert/delete in middle:    O(n)

    Wiki: http:://en.wikipedia.org/wiki/Linked_list
"""


class NoSuchElementError(Exception):
    pass


class Element(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current != None:
            yield(current.value)
            current = current.next

    def insert_front(self, element):
        self.head = Element(element, self.head)
        if self.tail == None:
            self.tail = self.head

    def insert_back(self, element):
        if self.empty():
            self.insert_front(element)
        else:
            self.tail.next = self.tail = Element(element, None)

    def insert_after(self, existing, element):
        existing_node = self.find(existing)
        if existing_node == None:
            raise NoSuchElementError
        existing_node.next = Element(element, existing_node.next)

    def delete(self, element):
        node = self.head
        previous = None
        while node != None and node.value != element:
            previous = node
            node = node.next
        if node == None:
            raise NoSuchElementError
        if node == self.tail:
            self.tail = previous
        if node == self.head:
            self.head = node.next
        else:
            previous.next = node.next

    def find(self, element):
        current = self.head
        while current != None and current.value != element:
            current = current.next
        return current

    def empty(self):
        return self.head == None
