class Solution:

    def encode(self, strs: List[str]) -> str:
        total = ""
        for x in strs:
            total += str(len(x)) + '#' + x
        return total

    def decode(self, s: str) -> List[str]:
        #.    4#neet4#code4#love3#you
        x = 0
        stringNumber = ''
        output = []
        while x < len(s):
            j = x
            while s[j] != '#':
                stringNumber += s[j]
                j += 1
            tracker = int(stringNumber)
            output.append(s[j+1:j+1+tracker])
            x = j+1+tracker
            stringNumber = ''
        return output

            

