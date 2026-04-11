from itertools import islice

def sliding_window(iterable, n):
    it = iter(iterable)
    window = tuple(islice(it, n))
    if len(window) == n:
        yield window
    for x in it:
        window = window[1:] + (x,)
        yield window