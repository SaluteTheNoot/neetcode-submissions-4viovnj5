class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #array of strings, must group together based on anagram (any order)
        anagrams = {}
        #iterate throughout strs:
            #if sorted(str) in anagrams:
                #anagrams[sorted(str)].append(str)
            #else:
                #anagrams[sorted(str)] = [str]
        #return anagrams

        for s in strs:
            joined = ''.join(sorted(s))
            if joined in anagrams:
                anagrams[joined].append(s)
            else:
                anagrams[joined] = [s]
        return anagrams.values()

        