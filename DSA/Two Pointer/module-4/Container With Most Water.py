class Solution:
    def maxArea(self, arr):
        left = 0
        right = len(arr)-1
        max_area =0
        while left < right:
            min_line = arr[left] if arr[left] < arr[right] else arr[right]
            current_area = min_line * (right - left)
            if current_area > max_area:
                max_area = current_area
            if arr[left] > arr[right]:
                right -= 1
            else:
                left += 1
        return max_area
        