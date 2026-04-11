from itertools import accumulate, chain, pairwise

class DifferenceArray:
    @staticmethod
    def build(arr):
        if not arr:
            return []
        return list(chain([arr[0]], (b - a for a, b in pairwise(arr))))

    @staticmethod
    def update(D, L, R, val):
        D[L] += val
        if R + 1 < len(D):
            D[R + 1] -= val

    @staticmethod
    def restore(D):
        return list(accumulate(D))