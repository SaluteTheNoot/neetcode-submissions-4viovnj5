class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for x in nums:
            hashmap[x] = 1 + hashmap.get(x,0)
        newHashmap = {}
        for x,y in hashmap.items():
            if y in newHashmap:
                newHashmap[y].append(x)
            else:
                newHashmap[y] = [x]
        largest = sorted(newHashmap.keys(), reverse = True)
        output = []
        for z in largest:
            output.extend(newHashmap[z])
            if len(output) == k:
                return output