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

# Áp dụng để tính Max Sum như code của bạn:
arr = [1, 2, 3, 4, 5, 6]
k = 3
max_sum = max(sum(w) for w in sliding_window(arr, k))
print(max_sum) # Kết quả: 15 (tổng của 4, 5, 6)