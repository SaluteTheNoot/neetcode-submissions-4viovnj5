from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #iterate through an array and group by anagram
            #aangram = letters and # of occurences of each letter
        #in order to see if words are anagrams, sort
        hashMap = defaultdict(list)

        for word in strs:
            sortWord = "".join(sorted(word))
            hashMap[sortWord].append(word)
        return hashMap.values()

        