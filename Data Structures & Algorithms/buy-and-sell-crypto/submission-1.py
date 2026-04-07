class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        num = prices[0]
        for x in range(1,len(prices)):
            if prices[x] < num:
                num = prices[x]
            else:
                profit = max(profit,prices[x]-num)
        return profit
        