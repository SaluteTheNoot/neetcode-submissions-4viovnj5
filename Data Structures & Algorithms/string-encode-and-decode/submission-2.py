class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for x in strs:
            output += str(len(x)) + '#' + x
        return output


    def decode(self, s: str) -> List[str]:
        index = 0
        stringNum = ''
        output = []
        while index < len(s):
            if s[index] != '#':
                stringNum += str(s[index])
                index += 1
            elif s[index] == '#':
                num = int(stringNum)
                output.append(s[index+1:index+num+1])
                index += num+1
                stringNum = ''
        return output



