from itertools import accumulate

class PrefixSum:
    def __init__(self, arr):
        self.P = [0] + list(accumulate(arr))

    def query(self, L, R):
        if L < 0 or R >= len(self.P) - 1 or L > R:
            raise IndexError("Invalid range")

        return self.P[R + 1] - self.P[L]