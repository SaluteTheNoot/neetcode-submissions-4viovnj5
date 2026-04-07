class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        for l in s:
            dicS[l] = dicS.get(l,0) + 1
        for l in t:
            dicT[l] = dicT.get(l,0) + 1
        return dicS == dicT
        