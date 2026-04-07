class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #figure out # of instances per number
        instanceMap = {}
        for num in nums:
            instanceMap[num] = instanceMap.get(num,0) + 1
        
        
        #hashmap has instances as key and value would be the numbers
        hashMap = {}
        for key, value in instanceMap.items():
            if value in hashMap:     
                hashMap[value].append(key)
            else:
                hashMap[value] = [key]

        #return k last keys in dictionary
        keys = sorted(hashMap.keys())
        
        output = []
        while len(output) < k:
            key = keys.pop()
            output.extend(hashMap[key])
        return output
        