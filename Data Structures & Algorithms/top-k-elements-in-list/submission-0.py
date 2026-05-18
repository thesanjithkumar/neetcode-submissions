from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        occur = defaultdict(int)
        for i in nums:
            occur[i] += 1

        sort_occur = dict(sorted(occur.items(), key=lambda item: item[1], reverse=True))

        return list(sort_occur.keys())[0:k]

