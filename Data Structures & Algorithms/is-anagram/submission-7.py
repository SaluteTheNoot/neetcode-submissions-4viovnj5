class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for x in s:
            hashS[x] = hashS.get(x,0) + 1
        for y in t:
            hashT[y] = hashT.get(y,0) + 1
        return hashS == hashT