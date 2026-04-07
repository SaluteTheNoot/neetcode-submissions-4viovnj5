class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            sort = ''.join(sorted(x))
            if sort in hashmap:
                hashmap[sort].append(x)
            else:
                hashmap[sort] = [x]
        return hashmap.values()