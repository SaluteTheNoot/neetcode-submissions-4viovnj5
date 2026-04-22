class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1,0,2,1,0,0,2,1,1,0,2,1]
        #[0,1]
        l,i,r = len(nums)-1,len(nums)-1,0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp


        while i >= r:
            #if i == 0, then swap and shift zero barrier over
            #if i == 2, then swap and shift two barrier over
            if nums[i] == 0:
                swap(i,l)
                l -= 1
            if nums[i] == 2:
                swap(i,r)
                r += 1
                i += 1
            
            i -= 1
        nums.reverse() 
