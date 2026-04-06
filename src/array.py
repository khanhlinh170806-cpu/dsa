class Array:
    """
    Cấu trúc dữ liệu Mảng (Array) tự cài đặt hoàn chỉnh.
    """

    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.size = 0
        self._data = [None] * capacity

    # --- NHÓM TRUY CẬP & TRẠNG THÁI ---
    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def _check_bounds(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError(f"Chỉ số {index} ngoài giới hạn.")

    def get(self, index: int):
        self._check_bounds(index)
        return self._data[index]

    def set(self, index: int, value) -> None:
        self._check_bounds(index)
        self._data[index] = value

    # --- NHÓM THAY ĐỔI CẤU TRÚC (TRỌNG TÂM) ---
    def _resize(self, new_capacity: int) -> None:
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self._data[i]
        self._data = new_data
        self.capacity = new_capacity

    def insert(self, index: int, value) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Chỉ số chèn không hợp lệ.")
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        # Shifting right
        for i in range(self.size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]
        self._data[index] = value
        self.size += 1

    def append(self, value) -> None:
        self.insert(self.size, value)

    def remove(self, index: int) -> None:
        self._check_bounds(index)
        # Shifting left
        for i in range(index, self.size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self.size - 1] = None 
        self.size -= 1

    # --- NHÓM DUYỆT, TÌM KIẾM & BIẾN ĐỔI ---
    def traverse(self) -> list:
        """Trả về một list chứa các phần tử thực tế (để in/debug)."""
        return [self._data[i] for i in range(self.size)]

    def find(self, value) -> int:
        """Tìm vị trí đầu tiên của value. (O(N))"""
        for i in range(self.size):
            if self._data[i] == value:
                return i
        return -1

    def reverse(self) -> None:
        """Đảo ngược mảng tại chỗ bằng 2 con trỏ. (O(N))"""
        left, right = 0, self.size - 1
        while left < right:
            self._data[left], self._data[right] = self._data[right], self._data[left]
            left += 1
            right -= 1