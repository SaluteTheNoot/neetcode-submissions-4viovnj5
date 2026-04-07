class Solution:
    def rob(self, nums: List[int]) -> int:
        #cannot rob adjacent homes
        [30,9,8,30,6]
        [9,30,8,6,30]
        [1,5,3]
        mon1,mon2 = 0,0
        for x in nums:
            hold = mon2
            mon2 = max(x+mon1,mon2)
            mon1 = hold
        return mon2