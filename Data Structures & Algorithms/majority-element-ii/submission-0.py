class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        #array of size n
        #return elements that appear more than n//3 times
        
        #steps:
        #we get size n
        #we count with hashSet and while adding
            #if more than n//3, add to set
        
        #return list(set)


        hashMap = defaultdict(int)
        size = len(nums)//3+1
        output = []


        for num in nums:
            hashMap[num] += 1
            if hashMap[num] == size:
                output.append(num)
        
        return output



