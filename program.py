"""Program code"""

# System Imports

# First Party Imports
from data_structures import LinkedList
from employee import Employee

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
    print(linked_list)
    linked_list.remove_from_front()
    linked_list.remove_from_back()
    print(linked_list)

    employee_list = LinkedList()
    employee_list.add_to_front(Employee("David", "Barnes", 750.00))
    employee_list.add_to_back(Employee("Jean", "Luc", 500.00))
    print(employee_list)
