class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #have an array of prices of ith day
        #want to return max profit by buying and selling once
        #you can store prev minimum and compare when higher value arrives
        smallest = 101
        output = 0

        for price in prices:
            if price > smallest:
                output = max(output, price-smallest)
            else:
                smallest = price
        return output
        