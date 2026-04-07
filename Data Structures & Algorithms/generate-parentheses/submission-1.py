class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        # 1,0 -> 2,0 -> 3,3
        # 3,3 -> 3,2 -> 3,1 -> 3,0 -> 2,0 -> 2,1 -> 3,1 -> 3,2 -> 3,3
        #
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                print(stack)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                print(stack)
                stack.pop()

        backtrack(0, 0)
        return res
