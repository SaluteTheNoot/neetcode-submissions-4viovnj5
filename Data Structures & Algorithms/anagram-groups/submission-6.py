class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        #iterate through strs
        for x in strs:
            #if the sorted version of x is in hashMap, you can simply append
            sort = ''.join(sorted(x))
            if sort in hashMap:
                hashMap[sort].append(x)
            else:
                hashMap[sort] = [x]
        return hashMap.values()




        