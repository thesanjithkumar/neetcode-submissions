class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        res = False
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res = True
                break
        return res