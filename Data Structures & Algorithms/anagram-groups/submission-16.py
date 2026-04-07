class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #string array
        #output a 2d array with anagrams grouped together   
            #can be outputted in any order
        #you go through each of the strings, sort

        hashStorage = {}

        for string in strs:
            sort = "".join(sorted(string))
            if sort in hashStorage:
                hashStorage[sort].append(string)
            else:
                hashStorage[sort] = [string]
        
        return hashStorage.values()
