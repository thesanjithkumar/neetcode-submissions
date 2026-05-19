class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)

        stack = []

        for i, cur_temp in enumerate(temps):

            while stack and cur_temp > temps[stack[-1]]:

                prev_day = stack.pop()

                res[prev_day] = i - prev_day

            stack.append(i)

        return res