class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return the k most frequent appearing elemeent in nums, unique output
        #you need to:
            #1. create dictionary which counts freq of each number
            #2. create another dictionary sorting by frequency
            #3. output vals in dictionary from most to least freq
        
        freq = {}

        #step 1
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        sort_by_freq = {}

        #step 2
        for number, frequency in freq.items():
            if frequency in sort_by_freq:
                sort_by_freq[frequency].append(number)
            else:
                sort_by_freq[frequency] = [number]
        
        #step 3
        output = []
        keys = sorted(sort_by_freq.keys())
        while len(output) < k:
            index = keys.pop()
            output.extend(sort_by_freq[index])
        return output