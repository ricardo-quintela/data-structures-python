from inspect import stack
from queue import Empty, Full


class Node:
    def __init__(self, content, index:int, parent=None, child=None):
        """Constructor of the class Node

        Args:
            content (Any): the content of the node
            index (int): the index of the node
            parent (Node): the previous Node, default is None
            child (Node): the next node, default is None
        """
        self._content = content

        self._parent = parent
        self._child = child
        self._index = index

    def set_parent(self, parent):
        """Set the parent of the node to the given Node

        Args:
            parent (Node): the parent to set to the node
        """
        self._parent = parent


    def get_parent(self):
        """Returns the parent of the node

        Returns:
            Node: the parent of the node
        """
        return self._parent

    
    def set_child(self, child):
        """Set the child of the node to the given Node

        Args:
            child (Node): the child to set to the node
        """
        self._child = child


    def get_child(self):
        """Returns the child of the node

        Returns:
            Node: the child of the node
        """
        return self._child



    def set_index(self, index:int):
        """Set the index of the node to the given integer

        Args:
            index (int): the index to set to the node
        """
        self._index = index


    def get_index(self) -> int:
        """Returns the index of the node

        Returns:
            int: the index of the node
        """
        return self._index

    def set_content(self, content):
        """Sets the content of the node to the given data

        Args:
            content (Any): the content of the node
        """
        self._content = content


    def get_content(self):
        """Returns the content of the node

        Returns:
            Any: the content of the node
        """
        return self._content


class Stack:
    def __init__(self, size:int):
        """Contructor of the class Stack

        Args:
            size (int): the maximum size of the Stack
        """

        self.size = size
        
        self.stack_pointer = None


    def push(self, content):
        """Adds the content to the stack if its not full and lowers the stack pointer

        Raises:
            Full: if the stack is full

        Args:
            content (Any): the content to append to the stack
        """
        if self.stack_pointer == None:
            node = Node(content, 0)
            self.stack_pointer = node
            return

        if self.stack_pointer.get_index() + 1 == self.size:
            raise Full("Error while trying to add the element: the stack reached its bottom!")

        node = Node(content, self.stack_pointer.get_index() + 1, parent=self.stack_pointer)
        self.stack_pointer.set_child(node)
        self.stack_pointer = node


    def pop(self):
        """Destroys the last element of the stack and raises the stack pointer
        """
        self.stack_pointer = self.stack_pointer.get_parent()


    def get_node(self, index:int) -> Node:
        """Returns the node on the given index on the stack

        Args:
            index (int): the index of the node

        Raises:
            IndexError: if the index is wrong
            Empty: if the stack is empty

        Returns:
            Node: the node on the given index
        """
        if self.stack_pointer == None:
            raise Empty("The stack is empty!")

        if index > self.stack_pointer.get_index() or index < 0:
            raise IndexError()

        node = self.stack_pointer
        for i in range(self.stack_pointer.get_index() - index):
            node = node.get_parent()

        return node


    def get_node_content(self, index:int):
        """Returns the node content

        Args:
            index (int): the index of the node

        Raises:
            IndexError: If the index is invalid
            Empty: If the stack is empty

        Returns:
            Any: the content of the node on the given index
        """
        if self.stack_pointer == None:
            raise Empty("the stack is empty!")

        return self.get_node(index).get_content()


    def clear(self):
        """Clears the stack by setting the stack pointer to None
        """
        self.stack_pointer = None


    def __repr__(self) -> str:
        """Returns a string representation of the stack showing its content

        Returns:
            str: a string representation of the content of the stack
        """
        string = "{"
        for i in range(self.stack_pointer.get_index() + 1):
            string += "\"" + self.get_node_content(i).__repr__() + "\", "

        return string[:-2] + "}"
