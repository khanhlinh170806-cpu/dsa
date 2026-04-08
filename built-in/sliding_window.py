class SlidingWindow:
    @staticmethod
    def max_sum_fixed(arr, k):
        n = len(arr)
        if k <= 0 or n < k:
            return -1

        # initial window (built-in)
        window_sum = sum(arr[:k])
        max_sum = window_sum

        # sliding
        for i in range(n - k):
            window_sum += arr[i + k] - arr[i]
            max_sum = max(max_sum, window_sum)

        return max_sum

    @staticmethod
    def min_subarray_len(arr, target):
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right, val in enumerate(arr):
            current_sum += val

            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= arr[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

    @staticmethod
    def all_window_sums(arr, k):
        if k <= 0 or len(arr) < k:
            return []

        window_sum = sum(arr[:k])

        return [window_sum] + [
            (window_sum := window_sum - arr[i] + arr[i + k])
            for i in range(len(arr) - k)
        ]

    @staticmethod
    def max_average_fixed(arr, k):
        max_sum = SlidingWindow.max_sum_fixed(arr, k)
        return max_sum / k if max_sum != -1 else 0