class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2 points, left (points at 0) and right (points at len(s)-1).
        #check if left pointer is pointing towards an alnum value, same with right
        #If they do and arent the same when lowered, return false
        #else, iterate both upwards
        #When left is not less than right, break and return true

        l,r = 0, len(s)-1
        while l < r:
            if s[l].isalnum() == False:
                l += 1
            elif s[r].isalnum() == False:
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
        