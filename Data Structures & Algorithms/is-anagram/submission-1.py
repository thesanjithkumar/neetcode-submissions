class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for i in s:
            counter[i] = counter.get(i, 0) + 1

        for j in t:
            if (j not in counter) or counter[j] == 0:
                return False
            else:
                counter[j] -= 1

        return True