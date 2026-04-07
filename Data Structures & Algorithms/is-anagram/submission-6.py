class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for x in s:
            hashS[x] = 1 + hashS.get(x,0)
        for y in t:
            hashT[y] = 1 + hashT.get(y,0)
        print(hashS)
        print(hashT)
        return hashS == hashT 