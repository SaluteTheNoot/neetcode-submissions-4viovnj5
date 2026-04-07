class Solution:

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 or n == 3:
            return n
        tracker1 = 1
        tracker2 = 2
        for x in range(2,n-1):
            holder = tracker2
            tracker2 += tracker1
            tracker1 = holder
        return tracker1 + tracker2
