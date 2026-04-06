import pytest
from src.array import Array

def test_array_basic_info():
    """Kiểm tra các hàm tiện ích và trạng thái ban đầu."""
    arr = Array(5)
    assert arr.is_empty() is True
    assert len(arr) == 0
    
    arr.append(10)
    assert arr.is_empty() is False
    assert len(arr) == 1

def test_array_full_workflow():
    """Kiểm tra luồng hoạt động chính và tự động resize."""
    arr = Array(capacity=2)
    arr.append(10)
    arr.append(20)
    arr.append(30) # Gây ra resize từ 2 lên 4
    
    assert len(arr) == 3
    assert arr.get(2) == 30
    assert arr.capacity == 4

def test_find_element():
    """Kiểm tra chức năng tìm kiếm (Searching)."""
    arr = Array()
    arr.append(10)
    arr.append(20)
    arr.append(30)
    
    assert arr.find(20) == 1 #(chỉ số của số 20)
    assert arr.find(99) == -1 #(không tìm thấy)

def test_reverse_array():
    """Kiểm tra chức năng đảo ngược mảng (In-place reverse)."""
    arr = Array()
    for x in [1, 2, 3, 4]:
        arr.append(x)
    
    arr.reverse()
    # Sau khi reverse: [4, 3, 2, 1]
    assert arr.traverse() == [4, 3, 2, 1]
    assert arr.get(0) == 4
    assert arr.get(3) == 1

def test_traverse_and_set():
    """Kiểm tra duyệt mảng và cập nhật giá trị."""
    arr = Array()
    arr.append(5)
    arr.append(10)
    arr.set(0, 7) # Thay 5 bằng 7
    
    assert arr.traverse() == [7, 10]

def test_index_error():
    """Kiểm tra các trường hợp truy cập sai chỉ số."""
    arr = Array()
    arr.append(1)
    with pytest.raises(IndexError):
        arr.get(5)
    with pytest.raises(IndexError):
        arr.remove(5)