import pytest
from built_in.prefix_sum import build_prefix, query
import random

def test_basic():
    """
    Test truy vấn tổng đoạn cơ bản
    """
    arr = [1, 2, 3, 4, 5]
    P = build_prefix(arr)

    assert query(P, 1, 3) == 9


def test_full_range():
    """
    Test truy vấn toàn mảng
    """
    arr = [10, 20, 30]
    P = build_prefix(arr)

    assert query(P, 0, 2) == 60


def test_single_element():
    """
    Edge case: L = R
    """
    arr = [7, 8, 9]
    P = build_prefix(arr)

    assert query(P, 1, 1) == 8


def test_invalid_range():
    """
    Test các trường hợp lỗi:
    - L > R
    - L < 0
    - R vượt phạm vi
    """
    arr = [1, 2, 3]
    P = build_prefix(arr)

    with pytest.raises(IndexError):
        query(P, 2, 1)

    with pytest.raises(IndexError):
        query(P, -1, 2)

    with pytest.raises(IndexError):
        query(P, 0, 5)


def test_randomized_bruteforce():
    """
    Randomized testing:
    - So sánh với brute force (sum)
    - Đảm bảo tính độc lập với implementation
    """
    for _ in range(100):
        n = random.randint(1, 50)
        arr = [random.randint(-100, 100) for _ in range(n)]
        P = build_prefix(arr)

        for _ in range(20):
            L = random.randint(0, n - 1)
            R = random.randint(L, n - 1)

            expected = sum(arr[L:R+1])

            assert query(P, L, R) == expected


def test_all_negative():
    """
    Edge case:
    - Mảng toàn số âm
    """
    arr = [-1, -2, -3, -4]
    P = build_prefix(arr)

    assert query(P, 1, 3) == -9