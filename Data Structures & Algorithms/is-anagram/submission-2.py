from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for i, j in zip(list(s),list(t)):
            count_s[i] += 1
            count_t[j] += 1

        return count_s == count_t