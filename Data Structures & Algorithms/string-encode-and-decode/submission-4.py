class Solution:

    def encode(self, strs: List[str]) -> str:
        #converts array of strings into encoded single string
        #how to know when one string end and another starts?
        #You can't use a particular character to denote when it stops and ends
            #It may be part of the string itself
        #Instead, if you add the number of characters in string and then a #, it solves it
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        #to encode, go through while loop while not empty
        #take number until #, get string through number, continue on
        decoded = []
        index = 0
        while index < len(s):
            number = ""
            character = s[index]
            while character != '#':
                number += character
                index += 1
                character = s[index]
            if character == '#':
                index += 1
                length = int(number)
                string = s[index:index+length]
                decoded.append(string)
                index = index+length
        return decoded
