class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for i in strs:
            k = "".join(sorted(i))
            if k in group:
                group[k].append(i)
            else:
                group[k] = [i]
        
        return list(group.values())