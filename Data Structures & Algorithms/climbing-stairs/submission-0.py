class Solution:
    @staticmethod
    def fibbo(number):
        if number <= 1:
            return 1
        else:
            return Solution.fibbo(number - 1) + Solution.fibbo(number - 2)

    def climbStairs(self, n: int) -> int:
        return self.fibbo(n)
