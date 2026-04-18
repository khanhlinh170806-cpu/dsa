import pytest
from built_in.sliding_window import Windowing
import random


def brute_windows(arr, k):
    """
    Naive method:
    - Tạo window bằng slicing
    """
    return [tuple(arr[i:i+k]) for i in range(len(arr) - k + 1)]


def test_basic():
    """
    Test generator sliding window cơ bản
    """
    arr = [1, 2, 3, 4]
    k = 2

    assert list(Windowing.sliding(arr, k)) == [(1, 2), (2, 3), (3, 4)]


def test_sum_equivalence():
    """
    Test ứng dụng:
    - Tổng các window phải giống brute force
    """
    arr = [1, 2, 3, 4, 5]
    k = 3

    window_sums = [sum(w) for w in Windowing.sliding(arr, k)]
    brute = [sum(arr[i:i+k]) for i in range(len(arr) - k + 1)]

    assert window_sums == brute


def test_randomized():
    """
    Randomized testing:
    - So sánh toàn bộ window với brute force
    """
    for _ in range(100):
        n = random.randint(1, 50)
        k = random.randint(1, n)

        arr = [random.randint(-10, 10) for _ in range(n)]

        assert list(Windowing.sliding(arr, k)) == brute_windows(arr, k)


def test_edge_case_k_greater_than_n():
    """
    Edge case:
    - Khi k > n → không có window nào
    """
    arr = [1]
    k = 2

    assert list(Windowing.sliding(arr, k)) == []


def test_single_window():
    """
    Edge case:
    - k = n → chỉ có 1 window
    """
    arr = [1, 2, 3]
    k = 3

    assert list(Windowing.sliding(arr, k)) == [(1, 2, 3)]