from src.array import Array

class SlidingWindow:
    """
    Các kỹ thuật Cửa sổ trượt ứng dụng trong Competitive Programming.
    """

    @staticmethod
    def max_sum_fixed(custom_array: Array, k: int) -> int:
        """
        Tìm tổng lớn nhất của k phần tử liên tiếp (Fixed Window).
        Độ phức tạp: O(N)
        """
        n = len(custom_array)
        if n < k:
            return -1

        # 1. Tính tổng của cửa sổ đầu tiên
        current_window_sum = 0
        for i in range(k):
            current_window_sum += custom_array.get(i)

        max_sum = current_window_sum

        # 2. Trượt cửa sổ: Thêm phần tử bên phải, bớt phần tử bên trái
        for i in range(n - k):
            # i là phần tử sắp bị loại bỏ (bên trái)
            # i + k là phần tử sắp được thêm vào (bên phải)
            current_window_sum = current_window_sum - custom_array.get(i) + custom_array.get(i + k)
            if current_window_sum > max_sum:
                max_sum = current_window_sum

        return max_sum

    @staticmethod
    def min_subarray_len(custom_array: Array, target: int) -> int:
        """
        Tìm độ dài nhỏ nhất của mảng con có tổng >= target (Dynamic Window).
        Kỹ thuật Two Pointers (2 con trỏ). Độ phức tạp: O(N)
        """
        n = len(custom_array)
        min_len = float('inf')
        current_sum = 0
        left = 0

        for right in range(n):
            current_sum += custom_array.get(right)

            # Thu hẹp cửa sổ từ bên trái khi tổng vẫn thỏa mãn >= target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= custom_array.get(left)
                left += 1

        return min_len if min_len != float('inf') else 0