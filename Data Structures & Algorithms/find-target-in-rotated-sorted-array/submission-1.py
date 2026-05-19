class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Did we find the target?
            if nums[mid] == target:
                return mid
                
            # RULE 1: Is the LEFT half perfectly sorted?
            if nums[left] <= nums[mid]:
                # Is our target mathematically inside this perfectly sorted left half?
                if nums[left] <= target and target < nums[mid]:
                    # Target is here! Throw away the right side.
                    right = mid - 1
                else:
                    # Target is NOT here. Throw away the left side.
                    left = mid + 1
                    
            # RULE 2: If the left isn't sorted, the RIGHT half MUST be perfectly sorted.
            else:
                # Is our target mathematically inside this perfectly sorted right half?
                if nums[mid] < target and target <= nums[right]:
                    # Target is here! Throw away the left side.
                    left = mid + 1
                else:
                    # Target is NOT here. Throw away the right side.
                    right = mid - 1
                    
        # If the loop finishes and we haven't found it
        return -1
