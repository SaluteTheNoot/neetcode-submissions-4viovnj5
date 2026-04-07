class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #return majority element
        #can not make array , O(n) time

        count, output = 0,0


        for num in nums:
            if count == 0:
                output = num
           
            if output != num:
                count -= 1
            else:
                count += 1
        
        return output

        
        


        