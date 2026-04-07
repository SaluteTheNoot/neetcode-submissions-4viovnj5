class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        #assign values in nums into hashmap
        for x in nums:
            if x not in hashMap:
                hashMap[x] = 1
            else:
                hashMap[x] += 1
        #create hashMap that is sorted version of prev hashmap
        newHash = {}
        for x,y in hashMap.items():
            if y not in newHash:
                newHash[y] = [x]
            else:
                newHash[y].append(x)
        #output k most frequent elements
        frequency = sorted(newHash.keys(), reverse = True)
        output = []
        for x in frequency:
            output.extend(newHash[x])
            if len(output) == k:
                return output
       




        