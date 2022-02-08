from queue import Full
from LinkedList import LinkedList

class CircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()


    def add(self, content):
        """Adds a node to the circular linked list

        Args:
            content (Any): the content to add to the circular linked list
        """
        super().add(content)

        self._start_node.set_parent(self._last_node)
        self._last_node.set_child(self._start_node)



    def set_max_size(self, max_size:int):
        """Sets the max size of the circular linked list to the given size

        Args:
            max_size (int): the max size of the circular linked list
        """
        self.max_size = max_size

    def get_max_size(self) -> int:
        """Returns the max size of the circular linked list

        Returns:
            int: the max size of the linked list
        """
        return self.max_size