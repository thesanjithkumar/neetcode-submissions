class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current_set = set()
        for i in nums:
            if i in current_set:
                return True
            current_set.add(i)

        return False