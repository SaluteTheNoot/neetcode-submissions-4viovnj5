class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buying and selling however many times you want
        #can buy and sell on the same day
        #can only hold one stock at a time
        #return max profit
        #[7,1,5,3,6,4]

        lowest = 10001

        profit = 0

        for num in prices:
            if lowest < num:
                profit += num - lowest
            
            lowest = num
        

        return profit



        