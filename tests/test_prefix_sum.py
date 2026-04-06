import pytest
from src.array import Array
from src.prefix_sum import PrefixSum

def test_prefix_sum_basic():
    # 1. Khởi tạo mảng dữ liệu: [1, 2, 3, 4, 5]
    arr = Array()
    for i in range(1, 6):
        arr.append(i)
    
    # 2. Khởi tạo PrefixSum
    ps = PrefixSum(arr)
    
    # 3. Kiểm tra các truy vấn
    # Tổng từ index 0 đến 2: 1 + 2 + 3 = 6
    assert ps.query(0, 2) == 6
    # Tổng từ index 1 đến 3: 2 + 3 + 4 = 9
    assert ps.query(1, 3) == 9
    # Tổng cả mảng (0 đến 4): 15
    assert ps.query(0, 4) == 15

def test_prefix_sum_single_element():
    arr = Array()
    arr.append(10)
    ps = PrefixSum(arr)
    # Truy vấn tại đúng 1 vị trí
    assert ps.query(0, 0) == 10

def test_prefix_sum_invalid_range():
    arr = Array()
    arr.append(1)
    ps = PrefixSum(arr)
    with pytest.raises(IndexError):
        ps.query(2, 1) # L > R phải báo lỗi