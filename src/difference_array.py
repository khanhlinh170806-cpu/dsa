from src.array import Array

class DifferenceArray:
    """
    Kỹ thuật Mảng hiệu giúp cập nhật giá trị lên một đoạn [L, R] trong O(1).
    """
    def __init__(self, custom_array: Array):
        self.n = len(custom_array)
        self.original_array = custom_array
        # Mảng hiệu D có kích thước n + 1 để tránh lỗi chỉ số khi R + 1 = n
        self.D = [0] * (self.n + 1)
        
        # Khởi tạo mảng hiệu ban đầu: D[i] = A[i] - A[i-1]
        self.D[0] = custom_array.get(0)
        for i in range(1, self.n):
            self.D[i] = custom_array.get(i) - custom_array.get(i-1)

    def update(self, L: int, R: int, val: int) -> None:
        """
        Cộng 'val' vào tất cả các phần tử từ chỉ số L đến R.
        Độ phức tạp: O(1)
        """
        if L < 0 or R >= self.n or L > R:
            raise IndexError("Phạm vi cập nhật không hợp lệ.")
            
        self.D[L] += val
        if R + 1 < self.n:
            self.D[R + 1] -= val

    def get_result(self) -> list:
        """
        Khôi phục lại mảng sau các thao tác cập nhật.
        Độ phức tạp: O(N)
        """
        result = [0] * self.n
        result[0] = self.D[0]
        for i in range(1, self.n):
            result[i] = result[i-1] + self.D[i]
        return result