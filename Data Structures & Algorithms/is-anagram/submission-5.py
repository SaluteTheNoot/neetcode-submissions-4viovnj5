class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            hashS[s[x]] = hashS.get(s[x],0) +1
            hashT[t[x]] = hashT.get(t[x],0) +1
        return hashT == hashS
        