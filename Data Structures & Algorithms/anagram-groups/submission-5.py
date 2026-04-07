class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for x in strs:
            sort = ''.join(sorted(x))
            if sort in hashMap:
                hashMap[sort].append(x)
            else:
                hashMap[sort] = [x]
        return hashMap.values()



        