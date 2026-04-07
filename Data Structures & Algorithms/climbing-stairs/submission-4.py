class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        prev,curr = 1,2

        for val in range(2, n):
            temp = curr
            curr += prev
            prev = temp
        return curr