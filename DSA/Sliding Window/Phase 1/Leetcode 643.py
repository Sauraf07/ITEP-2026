class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:

        # First window
        current_sum = sum(arr[:k])
        max_sum = current_sum

        # Slide the window
        for i in range(k, len(arr)):
            current_sum = current_sum + arr[i] - arr[i - k]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum / k