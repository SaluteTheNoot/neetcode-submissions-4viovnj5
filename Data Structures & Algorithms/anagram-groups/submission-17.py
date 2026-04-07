class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #given array of strings
        #organize anagrams into sublists and return
            #can be in any order
            #anagram is same caharcters, can be differenct order
        
        #we have a dictionary which will have a sorted anagram as the key
            #if match add the word
            #if not make new entry into dictionary


        anagram_dict = {}

        for string in strs:
            ana_sort = "".join(sorted(string))
            if ana_sort in anagram_dict:
                anagram_dict[ana_sort].append(string)
            else:
                anagram_dict[ana_sort] = [string]
        
        return list(anagram_dict.values())

