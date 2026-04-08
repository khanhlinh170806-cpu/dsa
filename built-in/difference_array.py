from itertools import accumulate

class DifferenceArray:
    def __init__(self, arr):
        self.n = len(arr)
        self.D = [arr[0]] + [b - a for a, b in zip(arr, arr[1:])]

    def update(self, L, R, val):
        if L < 0 or R >= self.n or L > R:
            raise IndexError("Invalid range")

        self.D[L] += val
        if R + 1 < self.n:
            self.D[R + 1] -= val

    def result(self):
        return list(accumulate(self.D))