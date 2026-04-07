class Solution:
    def isValid(self, s: str) -> bool:
        #given string, need to see if brackets has valid open + ending
        #use stack to accept characters. 
            #If opening bracket, add.
            #elif closing bracket
                #if stack[-1] is opening brack of same type (use dictionary)
                    #stack.pop()
                #else:
                    #return False
        #return len(stack) == 0

        stack = []
        open_close = {"}":"{", "]":"[", ")":"("}

        for bracket in s:
            if bracket in open_close:
                if len(stack) < 1:
                    return False
                elif stack[-1] == open_close[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0
    
        