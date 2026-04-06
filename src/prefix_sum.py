class PrefixSum:
    """
    Prefix Sum data structure for fast range queries.
    """

    def __init__(self, arr):
        """
        Build prefix sum array.
        """
        self.prefix = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            self.prefix[i + 1] = self.prefix[i] + arr[i]

    def range_sum(self, left, right):
        """
        Get sum from index left to right (inclusive).
        """
        return self.prefix[right + 1] - self.prefix[left]