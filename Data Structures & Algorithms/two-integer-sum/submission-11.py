class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #array of nums
        #return indices such that both values add up to target, can't be same indeces
        #O(n)
        

        hashFound = {}

        for index, num in enumerate(nums):
            newNum = target-num
            if newNum in hashFound:
                return [hashFound[newNum],index]
            else:
                hashFound[num] = index
