class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,1,2,4]
        #[1,1,2,8] with [1,2,4,6]
        #[1,2,4,6]
        #[48,24,12,8]
        newNums = [1]
        newNums.extend(nums[0:len(nums)-1])
        track = 1
        for x in range(len(newNums)):
            hold = newNums[x]
            newNums[x] *= track
            track *= hold
        track = 1
        for x in range(len(nums)-1,0, -1):
            track *= nums[x]
            newNums[x-1] *= track
        return newNums




        