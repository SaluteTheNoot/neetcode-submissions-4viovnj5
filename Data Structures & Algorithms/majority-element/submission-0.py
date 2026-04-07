class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #return majority element
        #can not make array , O(n) time

        hashMap = {}
        total_len = len(nums)
        
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
            if hashMap[num] >= total_len/2:
                return num