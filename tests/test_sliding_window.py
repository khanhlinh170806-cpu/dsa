import pytest
from src.array import Array
from src.sliding_window import SlidingWindow

def test_max_sum_fixed_window():
    # Khởi tạo mảng: [2, 1, 5, 1, 3, 2]
    arr = Array()
    data = [2, 1, 5, 1, 3, 2]
    for x in data:
        arr.append(x)
    
    sw = SlidingWindow()
    # Với k = 3: 
    # [2, 1, 5] -> sum = 8
    # [1, 5, 1] -> sum = 7
    # [5, 1, 3] -> sum = 9 (Max)
    # [1, 3, 2] -> sum = 6
    assert sw.max_sum_fixed(arr, 3) == 9

def test_max_sum_fixed_invalid_k():
    arr = Array()
    arr.append(1)
    sw = SlidingWindow()
    # Trường hợp k lớn hơn độ dài mảng
    assert sw.max_sum_fixed(arr, 5) == -1

def test_min_subarray_len_dynamic():
    # Khởi tạo mảng: [2, 3, 1, 2, 4, 3]
    arr = Array()
    data = [2, 3, 1, 2, 4, 3]
    for x in data:
        arr.append(x)
    
    sw = SlidingWindow()
    target = 7
    # Các mảng con có tổng >= 7: [2,3,1,2], [5,1,2], [2,4,3], [4,3]...
    # Mảng con ngắn nhất là [4, 3] có độ dài là 2.
    assert sw.min_subarray_len(arr, target) == 2

def test_min_subarray_len_no_result():
    arr = Array()
    arr.append(1)
    arr.append(2)
    sw = SlidingWindow()
    # Tổng mảng chỉ là 3, không bao giờ đạt tới 100
    assert sw.min_subarray_len(arr, 100) == 0