class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        
        #prefix = [1,1,2,6]
        #[1,2,3,4]
        
        mult = 1
        
        for i in range(len(nums)-1,0,-1):
            mult *= nums[i] 
            prefix[i-1] *= mult
        return prefix


        
        