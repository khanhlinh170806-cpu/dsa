from itertools import accumulate

def build_prefix(arr):
    return [0] + list(accumulate(arr))

def query(prefix, L, R):
    if L < 0 or R >= len(prefix) - 1 or L > R:
        raise IndexError("Invalid range")
    return prefix[R + 1] - prefix[L]