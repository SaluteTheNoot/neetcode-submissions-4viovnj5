class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        one_count = 0
        two_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            if num == 1:
                one_count += 1
            if num == 2:
                two_count += 1
       
        index = 0
     
        for i in range(zero_count):
            nums[index] = 0
            index += 1
        for i in range(one_count):
            nums[index] = 1
            index += 1
        for i in range(two_count):
            nums[index] = 2
            index += 1
        
        return nums
        
        