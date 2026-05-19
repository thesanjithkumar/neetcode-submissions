class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        res = []

        for i in range(len(temp)):
            days_waited = 0

            for j in range(i+1, len(temp)):
                if temp[j] > temp[i]:
                    days_waited = j - i
                    break

            res.append(days_waited)

        return res