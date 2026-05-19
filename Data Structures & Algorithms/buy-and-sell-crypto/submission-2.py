class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = float('inf')

        for i in prices:
            if i < lowest_price:
                lowest_price = i
            else:
                profit = i - lowest_price
                max_profit = max(profit, max_profit)

        return max_profit