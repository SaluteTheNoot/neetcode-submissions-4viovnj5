class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #return smallest positive integers that is not in nums

        #O(n) time, O(1) space

        nums = sorted(nums)

        output = 1

        for num in nums:
            if output == num:
                output += 1

        return output


        