class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for x in strs:
            res += str(len(x)) + '#' + x
        return res
    def decode(self, s: str) -> List[str]:
        output = []
        numberTracker = ""
        number = 0
        x = 0
        while x < len(s):
            if s[x] != '#':
                numberTracker += s[x]
                x+=1
            elif s[x] == '#':
                number = int(numberTracker)
                output.append(s[x+1:x+number+1])
                x += number+1
                number = 0
                numberTracker = ""
        return output
