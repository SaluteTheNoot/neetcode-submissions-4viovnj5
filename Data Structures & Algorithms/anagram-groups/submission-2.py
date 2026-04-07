class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            if ''.join(sorted(x)) in hashmap:
                hashmap[''.join(sorted(x))].append(x)
            else:
                hashmap[''.join(sorted(x))] = [x]
        return hashmap.values()
        