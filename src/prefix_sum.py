from src.array import Array

class PrefixSum:
    """
    Ứng dụng Prefix Sum để truy vấn tổng đoạn (Range Sum Query) trong O(1).
    """
    def __init__(self, custom_array: Array):
        self.n = len(custom_array)
        # Tạo một mảng P có kích thước n + 1 để xử lý dễ dàng trường hợp L=0
        # P[i] sẽ lưu tổng của i phần tử đầu tiên
        self.P = [0] * (self.n + 1)
        
        # Xây dựng mảng cộng dồn: P[i] = P[i-1] + A[i-1]
        for i in range(1, self.n + 1):
            self.P[i] = self.P[i-1] + custom_array.get(i-1)

    def query(self, L: int, R: int) -> int:
        """
        Trả về tổng các phần tử từ chỉ số L đến R (bao gồm cả L và R).
        Công thức: Sum(L, R) = P[R+1] - P[L]
        """
        if L < 0 or R >= self.n or L > R:
            raise IndexError("Phạm vi truy vấn (L, R) không hợp lệ.")
            
        return self.P[R + 1] - self.P[L]