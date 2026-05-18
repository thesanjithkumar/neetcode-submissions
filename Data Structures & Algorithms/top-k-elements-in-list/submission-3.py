# from collections import defaultdict

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         nums.sort()
#         occur = defaultdict(int)
#         for i in nums:
#             occur[i] += 1

#         sort_occur = dict(sorted(occur.items(), key=lambda item: item[1], reverse=True))
    

#         return list(sort_occur.keys())[0:k]

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter creates a dictionary of counts: {1: 3, 2: 2, 3: 1}
        count = Counter(nums)
        
        # most_common(k) returns a list of tuples: [(1, 3), (2, 2)]
        # We just need to extract the keys (the numbers themselves)
        return [num for num, freq in count.most_common(k)]