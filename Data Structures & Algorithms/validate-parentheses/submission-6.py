class Solution:
    def isValid(self, s: str) -> bool:

        #go through string and append leftsided to stack
        #if come across right sided
            #corellating bracket not found in stack[-1] or empty, F
            #otherwise continue
        
        #return len(stack) == 0

        bracket_dict = {'}':'{',')':'(',']':'['}
        stack = []

        for char in s:
            if char not in bracket_dict:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != bracket_dict[char]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0

        