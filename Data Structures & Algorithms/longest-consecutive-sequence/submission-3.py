class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #find longest consequtive sequence of elements
        #return number of max consequtive elements
        #O(n) time

        #duplicate don't matter, so make into a set
        num = set(nums)

        #loop through num:
        output = 0
        for number in num:
            conseq = 1
            while number+1 in num:
                conseq += 1
                number += 1
            output = max(output, conseq)
        return output
            #while number+1 in num:
                #conseq += 1, number += 1
            #output = max(output, conseq)
        
        
        #return output
        