class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # Notice we use left < right instead of left <= right
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # The middle is strictly greater than the rightmost element.
                # The minimum MUST be to the right of mid.
                left = mid + 1
            else:
                # The right side is sorted properly.
                # The minimum is either at mid, or to the left of mid.
                right = mid
                
        # When left and right meet, they are pointing at the minimum element!
        return nums[left]
