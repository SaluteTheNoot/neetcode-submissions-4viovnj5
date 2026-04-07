class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        curr, prev = 2,1

        for _ in range(2,n):
            temp = curr
            curr += prev
            prev = temp
        return curr

        