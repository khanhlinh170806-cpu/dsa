class PrefixSum:
    """
    Prefix Sum dùng list built-in Python
    """

    def __init__(self, arr):
        self.n = len(arr)
        self.P = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.P[i] = self.P[i - 1] + arr[i - 1]

    def query(self, L, R):
        """
        Tính tổng từ L đến R (inclusive)
        """
        if L < 0 or R >= self.n or L > R:
            raise IndexError("Phạm vi không hợp lệ")

        return self.P[R + 1] - self.P[L]