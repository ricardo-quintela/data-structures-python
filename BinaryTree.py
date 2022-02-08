class BinaryTree:
    def __init__(self, content=None, left=None, right=None):
        self._left = left
        self._right = right
        self._content = content
        self._count = 1

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


    def set_left(self, node):
        """Sets the left branch to the given node

        Args:
            node (Node): the left node
        """
        self._left = node

    def get_left(self):
        """Returns the left branch of the node

        Returns:
            Node: the left branch of the node
        """
        return self._left


    def set_right(self, node):
        """Sets the right branch to the given node

        Args:
            node (Node): the right node
        """
        self._right = node

    def get_right(self):
        """Returns the right branch of the node

        Returns:
            Node: the right branch of the node
        """
        return self._right

    
    def set_count(self, count:int):
        """Sets the number of elements stored in the node

        Args:
            count (int): the number of elements stored in the node
        """
        self._count = count

    def get_count(self) -> int:
        """Returns the number of elements stored in the node

        Returns:
            int: the number of elements stored in the node
        """
        return self._count



    def add(self, content):
        """Adds an element to the binary tree

        Args:
            content (Any): the content to add to the binary tree (MUST BE COMPARABLE)
        """

        #empty tree
        if self._content == None:
            self._content = content
            return

        #content is in the node
        if content == self._content:
            self.set_count(self._count + 1)
            return

        #content goes to the left branch
        elif content < self._content:
            if self._left == None:
                self._left = BinaryTree()

            self._left.add(content)
            return

        #content goes to the right branch
        if self._right == None:
                self._right = BinaryTree()

        self._right.add(content)


    def get(self, pattern):
        """Finds all matches for a pattern in the tree

        Args:
            pattern (Any): the pattern to find on the tree (MUST BE COMPARABLE)
        """

        if pattern == self._content[0:len(pattern)]:
            print(self._content.__repr__() + ": " + str(self._count))


        #pattern is before the content
        elif pattern < self._content:

            #empty left branch
            if self._left == None:
                return

            #search on the left
            self._left.get(pattern)
            return

        if self._right == None:
            return

        self._right.get(pattern)

        


    def show_content(self):
        """Shows a string representation of the content of the tree
        """

        #show the node's left
        if self._left != None:
            self._left.show_content()

        #show the node content
        print(self._content.__repr__() + ": " + str(self._count))

        #show the right branch
        if self._right != None:
            self._right.show_content()
