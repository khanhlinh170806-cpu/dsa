from built_in.difference_array import DifferenceArray
import pytest
from itertools import accumulate

# ----------------------
# Test build()
# ----------------------

def test_build_basic():
    arr = [1, 3, 6, 10]
    D = DifferenceArray.build(arr)
    assert D == [1, 2, 3, 4]


def test_build_single_element():
    arr = [5]
    D = DifferenceArray.build(arr)
    assert D == [5]


def test_build_empty():
    arr = []
    D = DifferenceArray.build(arr)
    assert D == []


# ----------------------
# Test restore()
# ----------------------

def test_restore_basic():
    D = [1, 2, 3, 4]
    arr = DifferenceArray.restore(D)
    assert arr == [1, 3, 6, 10]


def test_restore_empty():
    D = []
    arr = DifferenceArray.restore(D)
    assert arr == []


# ----------------------
# Test update()
# ----------------------

def test_single_update():
    arr = [1, 2, 3, 4, 5]
    D = DifferenceArray.build(arr)

    DifferenceArray.update(D, 1, 3, 10)
    result = DifferenceArray.restore(D)

    assert result == [1, 12, 13, 14, 5]


def test_multiple_updates():
    arr = [0, 0, 0, 0, 0]
    D = DifferenceArray.build(arr)

    DifferenceArray.update(D, 0, 2, 5)
    DifferenceArray.update(D, 1, 4, 3)

    result = DifferenceArray.restore(D)

    assert result == [5, 8, 8, 3, 3]


def test_update_full_range():
    arr = [1, 1, 1]
    D = DifferenceArray.build(arr)

    DifferenceArray.update(D, 0, 2, 2)
    result = DifferenceArray.restore(D)

    assert result == [3, 3, 3]


def test_update_single_index():
    arr = [1, 2, 3]
    D = DifferenceArray.build(arr)

    DifferenceArray.update(D, 1, 1, 5)
    result = DifferenceArray.restore(D)

    assert result == [1, 7, 3]


# ----------------------
# Edge cases
# ----------------------

def test_update_last_index_boundary():
    arr = [1, 2, 3]
    D = DifferenceArray.build(arr)

    DifferenceArray.update(D, 2, 2, 5)
    result = DifferenceArray.restore(D)

    assert result == [1, 2, 8]


def test_no_change_update():
    arr = [1, 2, 3]
    D = DifferenceArray.build(arr)

    DifferenceArray.update(D, 1, 2, 0)
    result = DifferenceArray.restore(D)

    assert result == arr