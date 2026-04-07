class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #have an array with values
        #need to find two values in array that add to target
        #y
        numbers = {}
        for index,value in enumerate(nums):
            if target - value in numbers:
                return [numbers[target - value], index]
            else:
                numbers[value] = index


        