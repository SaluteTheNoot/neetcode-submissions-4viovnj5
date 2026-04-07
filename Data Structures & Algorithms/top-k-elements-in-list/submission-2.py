class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #store in hashmap, for x in nums
        hashmap = {}
        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1
        #Have number of instances per number, now store hashmap by instance
        freq = {}
        for i,j in hashmap.items():
            if j in freq:
                freq[j].append(i)
            else:
                freq[j] = [i]
        #assing kth most frequent elements to output
        output = []
        largest = sorted(freq.keys(), reverse = True)
        for x in largest:
            output.extend(freq[x])
            if len(output) == k:
                return output
        