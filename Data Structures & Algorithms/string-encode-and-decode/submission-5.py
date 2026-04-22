class Solution:

    def encode(self, strs: List[str]) -> str:
        #list of string
        #length of string + & + string

        total_string = ""

        for string in strs:
            total_string += str(len(string)) + '&' + string
        
        return total_string[::-1]
    
    def decode(self, s: str) -> List[str]:
        string_array = []

        while len(s) > 0:
            stringNumber = ""
            
            while s[-1] != '&':
                stringNumber += s[-1]
                s = s[:-1]
            
            s = s[:-1]
            
            realNumber = int(stringNumber)
            word = ""
            
            for x in range(realNumber):
                word += s[-1]
                s = s[:-1]
            string_array.append(word)
        
        return string_array

