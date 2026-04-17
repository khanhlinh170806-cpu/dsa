from itertools import islice, chain
try:
    from itertools import batched as fixed_window_builtin
except ImportError:
    fixed_window_builtin = None

class Windowing:
    @staticmethod
    def sliding(iterable, n):
        it = iter(iterable)
        window = tuple(islice(it, n))
        if len(window) == n:
            yield window
        for x in it:
            window = window[1:] + (x,)
            yield window

    @staticmethod
    def fixed(iterable, n):
        if fixed_window_builtin:
            yield from fixed_window_builtin(iterable, n)
        else:
            it = iter(iterable)
            while True:
                batch = tuple(islice(it, n))
                if not batch:
                    break
                yield batch