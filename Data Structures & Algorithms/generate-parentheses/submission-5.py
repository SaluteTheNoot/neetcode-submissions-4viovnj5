class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n pairs of parentheses, output all combos of parentheses
        # n = w
            #output: ["((()))","(()())","(())()","()(())","()()()"]
        output = []
        stack = []
            #max out open parenthesis, then backtrack
        def backtrack(opened, closed):
            if opened < n:
                stack.append("(")
                backtrack(opened+1,closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed+1)
                stack.pop()
            if opened == closed == n:
                output.append("".join(stack))
        backtrack(0,0)
        return output

        