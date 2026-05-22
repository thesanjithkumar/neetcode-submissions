class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}

        for i, v in enumerate(nums):
            comp = target - v
            if comp in hashSet:
                return [hashSet[comp], i]
            hashSet[v] = i