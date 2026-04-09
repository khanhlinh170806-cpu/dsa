from itertools import islice

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = list(islice(it, n))
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.pop(0)
        window.append(x)
        yield tuple(window)