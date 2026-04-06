from src.prefix_sum import PrefixSum

def test_range_sum():
    arr = [1, 2, 3, 4]
    ps = PrefixSum(arr)

    assert ps.range_sum(0, 2) == 6
    assert ps.range_sum(1, 3) == 9