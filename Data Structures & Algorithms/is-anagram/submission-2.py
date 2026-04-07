class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sVar = {}
        tVar = {}
        for x in range(len(s)):
            sVar[s[x]] = 1 + sVar.get(s[x],0)
            tVar[t[x]] = 1 + tVar.get(t[x],0)
        return sVar == tVar

        

        