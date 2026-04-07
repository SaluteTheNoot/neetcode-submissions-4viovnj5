class Solution:
    def isPalindrome(self, s: str) -> bool:
        #have left, right pointer
        #check if both isalnum
            #if not, iterate the non isalnum
            #if so, lower both and see if they ==
                #if not, return False
                #if so, iterate both by 1
        #return True

        l,r = 0, len(s)-1

        while l < r:
            sL = s[l]
            sR = s[r]
            if sL.isalnum() == False:
                l += 1
            elif sR.isalnum() == False:
                r -= 1
            else:
                if sL.lower() != sR.lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True
        