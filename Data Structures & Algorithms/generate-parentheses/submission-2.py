class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def recursion(openP, closeP):
            if openP == closeP == n:
                result.append(''.join(stack))
                return
            if openP < n:
                stack.append('(')
                recursion(openP+1,closeP)
                stack.pop()
            if closeP < openP:
                stack.append(')')
                recursion(openP,closeP+1)
                stack.pop()
        recursion(0,0)
        return result


        