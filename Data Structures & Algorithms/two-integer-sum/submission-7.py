from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = defaultdict(int)

        for i, n in enumerate(nums):
            if target - n in s:
                return [s[target-n], i]
            else:
                s[n] = i