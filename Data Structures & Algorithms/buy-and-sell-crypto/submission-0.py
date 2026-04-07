class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 101
        bestReturn = 0
        for x in prices:
            minPrice = min(minPrice,x)
            bestReturn = max(bestReturn, x-minPrice)
        return bestReturn
