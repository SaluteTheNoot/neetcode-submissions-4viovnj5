class Solution:
    def isValid(self, s: str) -> bool:
        #go through string
        #if closing character
            #return false if stack[-1] does not have open version
            #else pop and continue
        #return true



        close_brack = {"]":"[","}":"{",")":"("}

        stack = []

        for character in s:
            if character in close_brack:
                if len(stack) == 0 or stack[-1] != close_brack[character]:
                    return False
                else:
                    stack.pop()
            
            else:
                stack.append(character)
        
        if len(stack) == 0:
            return True
        else:
            return False
        