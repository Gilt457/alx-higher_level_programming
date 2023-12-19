#!/usr/bin/python3

"""Classes for a singly-linked list."""


class Node:
    """A node in a singly-linked list."""

    def __init__(self, data, next=None):
        """Create a new Node.

        Args:
            data (int): The Node's data.
            next (Node): The Node's next node.
        """
        self.data = data
        self.next = next

    @property
    def data(self):
        """Get or set the Node's data."""
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next(self):
        """Get or set the Node's next node."""
        return self._next

    @next.setter
    def next(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next must be a Node object")
        self._next = value


class SinglyLinkedList:
    """A singly-linked list."""

    def __init__(self):
        """Create a new SinglyLinkedList."""
        self._head = None

    def sorted_insert(self, value):
        """Add a new Node to the SinglyLinkedList.

        The Node is added at the right numerical position.

        Args:
            value (Node): The Node to add.
        """
        node = Node(value)
        if self._head is None:
            node.next = None
            self._head = node
        elif self._head.data > value:
            node.next = self._head
            self._head = node
        else:
            current = self._head
            while (current.next is not None and
                    current.next.data < value):
                current = current.next
            node.next = current.next
            current.next = node

    def __str__(self):
        """Print the SinglyLinkedList."""
        values = []
        current = self._head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return ('\n'.join(values))
