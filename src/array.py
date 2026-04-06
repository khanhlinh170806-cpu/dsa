#viết class
class Array:
    """
    A simple implementation of a dynamic array.

    Attributes:
        capacity (int): Total capacity of the array
        size (int): Current number of elements
        data (list): Internal storage
    """

    def __init__(self, capacity=2):
        """
        Initialize array with given capacity.
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def __len__(self):
        return self.size

    def get(self, index):
        """
        Get element at index.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def append(self, value):
        """
        Add element to the end.
        """
        if self.size == self.capacity:
            self._resize()

        self.data[self.size] = value
        self.size += 1

    def _resize(self):
        """
        Double the capacity of the array.
        """
        self.capacity *= 2
        new_data = [None] * self.capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data

    def remove(self, index):
        """
        Remove element at index.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1