from src.array import Array

def test_append():
    arr = Array()
    arr.append(1)
    arr.append(2)

    assert arr.get(0) == 1
    assert arr.get(1) == 2

def test_remove():
    arr = Array()
    arr.append(1)
    arr.append(2)
    arr.remove(0)

    assert arr.get(0) == 2