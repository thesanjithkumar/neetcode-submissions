class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        # Keep searching as long as our search window is valid
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # We found it!
                
            elif nums[mid] < target:
                # The middle number is too small. 
                # The target MUST be in the right half.
                # So, we move our left boundary past the middle.
                left = mid + 1
                
            else:
                # The middle number is too big.
                # The target MUST be in the left half.
                # So, we move our right boundary before the middle.
                right = mid - 1
                
        # If the loop finishes and we haven't returned, the target isn't there
        return -1
