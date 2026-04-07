class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #two strings
        #if anagrams, return true else false
            #anagram is string that has exact same characters as other string but diff order
        
        #we need to check that the freq of characters is same for both
            #if so return true
            #otherwise false
        #can be done with a dictionary

        dictS = {}
        dictT = {}

        for character in s:
            dictS[character] = dictS.get(character,0) + 1

        for character in t:
            dictT[character] = dictT.get(character,0) + 1
        
        return dictS == dictT
        
        