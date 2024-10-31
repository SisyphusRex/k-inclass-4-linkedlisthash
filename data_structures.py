"""Data Structures"""


class LinkedList:
    """linked list data structure"""

    # has-a relationship
    class Node:
        """node in a data structure"""

        def __init__(self):
            """constructor"""
            self.data = None
            self.next = None

    def __init__(self):
        """Counstructor"""
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def is_empty(self):
        """Whether the linked list is empty or not"""
        return self._head is None

    @property
    def size(self):
        """property for size"""
        return self._size

    def add_to_front(self, data):
        """Add a new element to the front of the linked list"""
        # Make a new variable to also reference the head of the list
        old_head = self._head
        # Make a new node and assign it ot the head variable
        self._head = self.Node()
        # set the data on the new node
        self._head.data = data
        # Make the next property of the node point ot the old head
        self._head.next = old_head
        # incremnt the size of the list
        self._size += 1
        # enshure that if we are adding the very first node to the linked list
        # that the tail will be pointing to the new node we create
        if self._size == 1:
            self._tail = self._head

    def add_to_back(self, data):
        """add a new element to the back of the linked list O(1)"""
        # make a pointer to the old tail
        old_tail = self._tail
        # make a new node and assign it to back
        self._tail = self.Node()
        # add data to new node
        self._tail.data = data

        # increment size
        self._size += 1
        # if list was empty, make head point to this
        if self._size == 1:
            self._head = self._tail
        else:
            # point old tail to tail
            old_tail.next = self._tail

    def remove_from_front(self):
        """Remove an element from th efront of the linked list O(1)"""
        # check if only element and remove tail pointer if so
        if self.is_empty:
            raise IndexError("Nothing to remove.  List is empty.")

        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        if self.is_empty:
            self._tail = None
        return data

    def remove_from_back(self):
        """Remove an element from the back of the linked list"""
        if self.is_empty:
            raise IndexError("Nothing to remove. List is empty.")
        data = self._tail.data
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.next != self._tail:
                current = current.next
            self._tail = current
            self._tail.next = None
        self._size -= 1
        return data

    def get_data_at_index(self, index):
        """method to get data at index"""
        if self.is_empty:
            raise IndexError("Nothing in Linked List.")
        counter: int = 0
        current_node = self._head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node.data

    def __str__(self):
        """String method.  Display the contents of the linked lists"""
        my_string = ""
        current = self._head
        while current is not None:
            my_string = my_string + f"{current.data}\n"
            current = current.next
        return my_string


class HashTable:
    """Basic hash table data structure"""

    PRIME_VALUE = 97

    # TODO: Add buckets consisting of linked lists to self._values list and handle collisions
    def __init__(self):
        """constructor"""
        self._values = [None for i in range(self.PRIME_VALUE)]
        self._keys = [None for i in range(self.PRIME_VALUE)]

    def put(self, key, value) -> None:
        """Put something into hash table"""
        index_for_value = self.__hash_function(key)
        self._values[index_for_value] = value
        self._keys[index_for_value] = key

    def get(self, key) -> int:
        """get something from the hash table"""
        index_for_value = self.__hash_function(key)
        return self._values[index_for_value]

    def __hash_function(self, key) -> int:
        """hash key to index"""
        try:
            hash_value = hash(key) % self.PRIME_VALUE
        except TypeError:
            hash_value = id(key) % self.PRIME_VALUE
        return hash_value

    def __str__(self):
        """String method"""
        return_string = "Key   => Value\n"
        return_string += "--------------\n"
        for i in range(self.PRIME_VALUE):
            if self._values[i] is not None:
                return_string += f"{self._keys[i]} => {self._values[i]}\n"
        return return_string

    def show_array(self):
        """show underlying array"""
        return_string = "Key => Value\n"
        return_string += "------------\n"
        for i in range(self.PRIME_VALUE):
            value = ""
            if self._values[i] is not None:
                value = self._values[i]
            return_string += f"[{i}] => {value}\n"
        return return_string
