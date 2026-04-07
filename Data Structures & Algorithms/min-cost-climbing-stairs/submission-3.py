class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        [1,2,1,2,1,1,1]
        for x in range(len(cost)-3,-1,-1):
            cost[x] += min(cost[x+1],cost[x+2])
        return min(cost[0],cost[1])
