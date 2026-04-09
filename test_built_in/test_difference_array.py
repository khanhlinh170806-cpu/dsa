import pytest
from built_in.difference_array import build_diff, range_update, restore
import random

def brute_force(arr, updates):
    """
    Naive implementation:
    - Áp dụng update trực tiếp O(n^2)
    - Dùng làm oracle để kiểm tra
    """
    res = arr[:]
    for L, R, val in updates:
        for i in range(L, R + 1):
            res[i] += val
    return res


def test_basic():
    """
    Test chức năng cơ bản:
    - Build difference array
    - Apply 1 range update
    - Restore lại mảng đúng
    """
    arr = [1, 2, 3, 4, 5]
    D = build_diff(arr)

    range_update(D, 1, 3, 2)

    assert restore(D) == [1, 4, 5, 6, 5]


def test_multiple_updates():
    """
    Test nhiều update chồng nhau:
    - Kiểm tra tính đúng của cumulative updates
    """
    arr = [0, 0, 0, 0, 0]
    D = build_diff(arr)

    range_update(D, 0, 2, 1)
    range_update(D, 1, 4, 2)

    assert restore(D) == [1, 3, 3, 2, 2]


def test_randomized():
    """
    Randomized testing:
    - So sánh với brute force (oracle)
    - Đảm bảo đúng với nhiều trường hợp ngẫu nhiên
    """
    for _ in range(100):
        n = random.randint(1, 50)
        arr = [random.randint(-10, 10) for _ in range(n)]

        D = build_diff(arr)
        updates = []

        for _ in range(random.randint(1, 20)):
            L = random.randint(0, n - 1)
            R = random.randint(L, n - 1)
            val = random.randint(-5, 5)

            range_update(D, L, R, val)
            updates.append((L, R, val))

        assert restore(D) == brute_force(arr, updates)


def test_edge_case_single_element():
    """
    Edge case:
    - Mảng chỉ có 1 phần tử
    """
    arr = [5]
    D = build_diff(arr)

    range_update(D, 0, 0, 3)

    assert restore(D) == [8]