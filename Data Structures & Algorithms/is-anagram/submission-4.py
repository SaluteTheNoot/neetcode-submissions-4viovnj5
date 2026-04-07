class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            hashS[s[x]] = 1 + hashS.get(s[x],0)
            hashT[t[x]] = 1 + hashT.get(t[x],0)
        return hashS == hashT

        
        