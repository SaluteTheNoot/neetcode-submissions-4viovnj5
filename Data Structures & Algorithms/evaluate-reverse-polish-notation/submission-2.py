class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #have an array with polish notation
        #values calculated from left to right, with math operators
        #division truncates towards zero (negative round up, positive round down)

        #can do this using a stack
        #continue appending until you reach operator
            #pop twice and do math on popped values based on operator
            #append this new value
        #return final value in stack

        stack = []
        for token in tokens:
            if token == '+':
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum + firstNum)
            elif token == '-':
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum - firstNum)
            elif token == '*':
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum * firstNum)
            elif token == '/':
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(int(secondNum/firstNum))
            else:
                stack.append(int(token))
        return stack[0]
        