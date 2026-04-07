class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        test = set()
        for x in nums:
            if x-1 not in num:
                test.add(x)
        
        maxSeq = 1
        if len(nums) == 0:
            return 0
        for x in test:
            track = 1
            while x+1 in num:
                track += 1
                x += 1
            maxSeq = max(maxSeq,track)
        return maxSeq

                

        