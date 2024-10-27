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


class MergeSort:
    """Merge Sort Class"""

    def __init__(self):
        """constructor"""
        self._aux: list = []

    def sort(self, input_list: list) -> None:
        """main merge sort method"""
        self._aux = [None for i in range(len(input_list))]
        self._sort(input_list, 0, len(input_list) - 1)

    def _sort(self, sortable: list, low: int, high: int) -> None:
        """recursive method"""
        if high <= low:
            return
        mid: int = low + int((high - low) / 2)
        self._sort(sortable, low, mid)
        self._sort(sortable, mid + 1, high)
        self._merge(sortable, low, mid, high)

    def _merge(self, mergeable: list, low: int, mid: int, high: int) -> None:
        """merge method"""
        for k in range(low, high + 1):
            self._aux[k] = mergeable[k]

        i: int = low
        j: int = mid + 1
        for k in range(low, high + 1):
            if i > mid:
                mergeable[k] = self._aux[j]
                j += 1
            elif j > high:
                mergeable[k] = self._aux[i]
                i += 1
            elif self._aux[j] < self._aux[i]:
                mergeable[k] = self._aux[j]
                j += 1
            else:
                mergeable[k] = self._aux[i]
                i += 1
        return
