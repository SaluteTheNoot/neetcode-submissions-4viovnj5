class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        #iterate throughout nums:
            #if target - num in numbers:
                #return index of both
            #else:
                #numbers[num] = index
        for index, num in enumerate(nums):
            find = target - num
            if find in numbers:
                return [numbers[find], index]
            else:
                numbers[num] = index
            