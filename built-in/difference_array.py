from itertools import accumulate

def build_diff(arr):
    return [arr[0], *(b - a for a, b in zip(arr, arr[1:]))]

def range_update(D, L, R, val):
    D[L] += val
    if R + 1 < len(D):
        D[R + 1] -= val

def restore(D):
    return list(accumulate(D))