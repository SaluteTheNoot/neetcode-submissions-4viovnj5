class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,4,6] -> [1,1,2,4] -> [1,1,2,8]
        #[1,2,4,6] -> [1,2,4,6]
        #[1,1,2,8] -> [1,1,6*2,8] -> [1,1*6*4,6*2,8] -> [1*2*4*6,1*6*4,6*2,8]
        # [48,24,12,8]
        array = [1]
        tracker = 1
        for x in range(0,len(nums)-1):
            array.append(nums[x]*tracker)
            tracker *= nums[x]
        tracker = 1
        for x in range(len(nums)-1, 0, -1):
            array[x-1] *= nums[x] * tracker
            tracker *= nums[x]
        return array



        