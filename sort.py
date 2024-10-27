"""sort module"""

# System Imports

# First Party Imports

# Third Party Imports


class BubbleSort:
    """Bubble Sort class"""

    def sort(self, sortable) -> None:
        """Method to perform bubble sort"""

        sortable_length: int = len(sortable)
        for i in range(sortable_length):
            for j in range(sortable_length):
                if sortable[j] > sortable[i]:
                    temp = sortable[i]
                    sortable[i] = sortable[j]
                    sortable[j] = temp
