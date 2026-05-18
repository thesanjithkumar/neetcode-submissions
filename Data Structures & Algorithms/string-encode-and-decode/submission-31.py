class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = ["/"+str(len(x)) for x in strs]
        strs = strs + ["~"] + lens
        print("".join(strs))
        return "".join(strs)
            

    def decode(self, s: str) -> List[str]:
        strs = []
        splits = s.split('~')
        print(splits[1].split("/")[1:])
        lens = [int(x) for x in splits[1].split("/")[1:]]
        current_sum = 0
        res = [0]
        for i in lens:
            current_sum += i
            res.append(current_sum)
        print(res)
        for i in range(0, len(res)-1, 1):
            # if i != len(res):
            strs.append(s[res[i]:res[i+1]])
        return strs