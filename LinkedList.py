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

    


class LinkedList:
    def __init__(self):
        """Constructor of the class LinkedList
        """

        #current size of the linked_list
        self.size = 0

        #the start node of the linked list
        self._start_node = None
        self._last_node = None

    
    def add(self, content):
        """Adds a node to the linked list

        Args:
            content (Any): the content to add to the linked list
        """
        node = Node(content, self.size)

        if self._start_node == None:
            self._start_node = node
            self._last_node = self._start_node

        else:
            node.set_parent(self._last_node)
            self._last_node.set_child(node)
            self._last_node = node

        self.size += 1


    def get_node(self, index:int) -> Node:
        """Returns the node at the given index

        Args:
            index (int): the index of the node

        Raises:
            IndexError: if the index is invalid

        Returns:
            Node: the node at the given index
        """
        if index >= self.size or index < 0:
            raise IndexError()

        node = self._start_node
        for i in range(index):
            node = node.get_child()

        return node


    def get_node_content(self, index:int):
        """Returns the content of a node at the given index

        Args:
            index (int): the index of the node

        Raises:
            IndexError: if the index is invalid

        Returns:
            Any: the content of the node at the given index
        """
        
        return self.get_node(index).get_content()


    def __repr__(self) -> str:
        """Returns a string representation of the linked list showing its content

        Returns:
            str: a string representation of the content of the linked list
        """
        string = "{"
        for i in range(self.size):
            string += "\"" + self.get_node_content(i).__repr__() + "\", "

        return string[:-1] + "}"
        

        