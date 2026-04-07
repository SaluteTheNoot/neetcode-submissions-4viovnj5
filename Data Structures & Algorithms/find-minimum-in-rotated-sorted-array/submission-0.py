class Solution:
    def findMin(self, nums: List[int]) -> int:
        #have an array that has been roatated between 1 and n (len of arr) times
        #originally sorted in ascending order
        #all elelemnts are unique
        #return min element in array in O(logn) time
        #we have to use binary search somehow to find min value
        
        #start in the middle of array.
        #m = (l+r)//2

        l,r = 0, len(nums) - 1
        m = (l+r)//2
        # no swapping occured (1,2,3,4,5,6,7)
        smallest = nums[m]
        if nums[l] < nums[r]:
            return nums[l]
        #if swapping has occured
        while l<=r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m-1
                smallest = min(smallest, nums[(l+r)//2])
            else:
                l = m+1
                smallest = min(smallest, nums[(l+r)//2])
        return smallest


        