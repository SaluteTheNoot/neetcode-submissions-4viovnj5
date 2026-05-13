class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            
            if len(count) <= 2:
                continue
            
            #subtract out the ones on just one
            else:
                new_count = defaultdict(int)
                for index,freq in count.items():
                    if freq > 1:
                        new_count[index] = freq-1
                    
                count = new_count
        
        result = []
        
        for index, freq in count.items():
            total = nums.count(index)
            if total > len(nums)//3:
                result.append(index)

        return result
