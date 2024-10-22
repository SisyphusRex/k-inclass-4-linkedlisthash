"""Program code"""

# System Imports

# First Party Imports
from data_structures import LinkedList

# Third Party Imports


def main(*args):
    """Method to run program"""
    # make instance of linked list
    linked_list = LinkedList()

    # add to the front and back a few times
    linked_list.add_to_front(5)
    linked_list.add_to_front(3)
    linked_list.add_to_back(6)
    linked_list.add_to_back(1)
    linked_list.add_to_front(9)
