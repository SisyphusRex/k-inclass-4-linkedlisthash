"""Program code"""

# System Imports

# First Party Imports
from data_structures import LinkedList, HashTable
from employee import Employee
from sort import BubbleSort

# Third Party Imports


def main(*args):
    """Method to run program"""
    # make instance of linked list
    linked_list = LinkedList()
    my_bubble = BubbleSort()
    my_list: list[int] = [4, 7, 2, 9, 5, 3]
    # add to the front and back a few times
    linked_list.add_to_front(5)
    linked_list.add_to_front(3)
    linked_list.add_to_back(6)
    linked_list.add_to_back(1)
    linked_list.add_to_front(9)

    linked_list.remove_from_front()
    linked_list.remove_from_back()

    employee_list = LinkedList()
    employee_list.add_to_front(Employee("David", "Barnes", 750.00))
    employee_list.add_to_back(Employee("Jean", "Luc", 500.00))

    found_employee = employee_list.get_data_at_index(1)

    my_bubble.sort(my_list)

    ########################
    # Hash Table Work      #
    ########################

    valley_number_to_name: HashTable = HashTable()
    print()
    print("Adding some entries to the HashTable")
    print("EX: valley_number_to_name.put(12345, 'David Barnes')")

    valley_number_to_name.put(12345, "Yeetus McMeetus")
    valley_number_to_name.put(12543, "Yep Erroo")
    valley_number_to_name.put(54321, "Poke Mon")
    valley_number_to_name.put(45321, "Pika Chu")
    valley_number_to_name.put(12354, "The Snorlax")

    print("The created hash table")
    # print(valley_number_to_name)
    # print(valley_number_to_name.show_array())
    print("************************")

    print("Get a single value from the hash table")
    print("valley_number_to_name.get(12345)")
    print(valley_number_to_name.get(12345))
    print()
    print("What if 2 entries collide?")
    print("EX: valley_number_to_name.put(26189, 'First Entry')")
    valley_number_to_name.put(26189, "First Entry")
    print("EX: valley_number_to_name.put(26092, 'Second Entry')")
    valley_number_to_name.put(26092, "Second Entry")

    # print(valley_number_to_name)
    # print(valley_number_to_name.get(26189))

    print("String keys:")
    string_hash_table = HashTable()
    string_hash_table.put("foobar", "joe Biggs")
    string_hash_table.put("barbaz", "Jim Giggles")
    print(string_hash_table)
