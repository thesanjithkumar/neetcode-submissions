class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s, sorted_t = sorted(s), sorted(t)
        return "".join(sorted_s) == "".join(sorted_t)