import pytest
from src.array import Array
from src.difference_array import DifferenceArray

def test_difference_array_update():
    arr = Array()
    for x in [10, 5, 20, 40]:
        arr.append(x)
    
    diff = DifferenceArray(arr)
    # Cộng 10 vào đoạn [1, 2] (giá trị 5 và 20)
    # Mảng mong muốn: [10, 15, 30, 40]
    diff.update(1, 2, 10)
    
    assert diff.get_result() == [10, 15, 30, 40]

def test_multiple_updates():
    arr = Array()
    for x in [0, 0, 0, 0, 0]:
        arr.append(x)
    
    diff = DifferenceArray(arr)
    diff.update(0, 4, 5)  # Cộng 5 cả mảng: [5, 5, 5, 5, 5]
    diff.update(1, 2, 2)  # Cộng 2 vào [1,2]: [5, 7, 7, 5, 5]
    
    assert diff.get_result() == [5, 7, 7, 5, 5]