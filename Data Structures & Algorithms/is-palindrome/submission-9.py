class Solution:
    def isPalindrome(self, s: str) -> bool:

        numbers = {"1","2","3","4","5","6","7","8","9","0"}
        string = ""

        

        for char in s:
            if char.isalnum():
                if char in numbers:
                    string += char
                else:
                    string += char.lower()
        
        return string == string[::-1]

        