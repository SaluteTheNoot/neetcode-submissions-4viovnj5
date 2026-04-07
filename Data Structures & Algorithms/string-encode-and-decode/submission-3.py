class Solution:

    def encode(self, strs: List[str]) -> str:
        #when encoding, you would have to put something at start
        #put length of the word before along with @
        string = ""
        for word in strs:
            string += str(len(word)) + '@'
            string += word
        return string

    def decode(self, s: str) -> List[str]:
        #take length, goes up until '@'
        #take the indexes from index '@'+1 to '@'+1+index [@+1:@+1+index]
        #adds word to an array and skips over to next number
        #stops when it reaches the end (while loop)
        x = 0
        output = []
        strNum = ''
        while x < len(s):
            if s[x] != "@":
                strNum += str(s[x])
                x += 1
            elif s[x] == "@":
                length = int(strNum)
                x += 1
                word = s[x:x+length]
                output.append(word)
                x += length
                strNum = ''
        return output


