class Solution:

    def climbStairs(self, n: int) -> int:
        def fibbo(number):
            if number <= 1:
                return 1
            else:
                return fibbo(number - 1) + fibbo(number - 2)
        return fibbo(n)
