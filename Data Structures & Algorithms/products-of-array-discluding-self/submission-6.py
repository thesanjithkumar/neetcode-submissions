class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        output = [1] * n
        
        # Step 1: Calculate prefix products and store in output
        prefix_product = 1
        for i in range(n):
            output[i] = prefix_product
            prefix_product *= nums[i]
            
        # Step 2: Calculate suffix products on the fly and multiply with prefix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]
            
        return output