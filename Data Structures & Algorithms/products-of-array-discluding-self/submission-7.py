class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        output = []

        for num in nums:
            if num != 0:
                total_product *= num
            elif num == 0:
                zero_count += 1
        

        if zero_count >= 2:
            return [0] * len(nums)
        
        
        
        elif zero_count == 1:
            for num in nums:
                if num != 0:
                    output.append(0)
                elif num == 0:
                    output.append(total_product)
        else:
            for num in nums:
                output.append(total_product // num)
         
        return output
            
        