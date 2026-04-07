class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for letter in s:
            hashS[letter] = 1 + hashS.get(letter,0)
        for letter in t:
            hashT[letter] = 1 + hashT.get(letter,0)
        return hashS == hashT