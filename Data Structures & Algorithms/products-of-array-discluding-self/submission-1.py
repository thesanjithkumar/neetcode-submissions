class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create an output array filled with 1s. 
        # Length is the same as nums.
        res = [1] * len(nums)
        
        # --- PASS 1: PREFIX (Left Products) ---
        # Keep a running product of elements to the left
        left_product = 1
        for i in range(len(nums)):
            # Store the left product in our result array
            res[i] = left_product
            # Update the left product by multiplying the current number
            left_product *= nums[i]
            
        # After Pass 1, res looks like this for [1, 2, 4, 6]:
        # res = [1, 1, 2, 8]
            
        # --- PASS 2: SUFFIX (Right Products) ---
        # Keep a running product of elements to the right
        right_product = 1
        for i in range(len(nums) - 1, -1, -1): # Loop backwards
            # Multiply the existing left product by the right product
            res[i] *= right_product
            # Update the right product by multiplying the current number
            right_product *= nums[i]
            
        return res