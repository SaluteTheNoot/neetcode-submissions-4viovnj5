class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #int array and integer val
        #remove all occurense of val from array in-place
        #return remaining elements

        for index in range (len(nums)-1, -1, -1):
            if nums[index] == val:
                nums.pop(index)
        
        return len(nums)
        