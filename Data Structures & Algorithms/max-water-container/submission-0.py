class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_i = 0
        right_i = len(heights) - 1
        max_area = 0
        while left_i < right_i:
            w = right_i - left_i
            min_height = min(heights[right_i], heights[left_i])
            area = min_height * w
            max_area = max(max_area, area)

            if heights[left_i] < heights[right_i]:
                left_i += 1

            else:
                right_i -= 1

        return max_area
