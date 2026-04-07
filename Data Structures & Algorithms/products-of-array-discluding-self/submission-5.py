class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #if there are two zeros
            #all are zero
        #if one zero:
            #all except for zero index zero, zero index is product of another elements
        #if no zero:
            #calcaulte total by multiplying all together
            #divive product by number at parituclar index
        
        zero_count = 0
        total = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total *= num
        
        output = []

        if zero_count == 0:
            for num in nums:
                output.append(total//num)

        elif zero_count == 1:
            for num in nums:
                if num == 0:
                    output.append(total)
                else:
                    output.append(0)
        
        else:
            output = [0] * len(nums)
        
        return output
        