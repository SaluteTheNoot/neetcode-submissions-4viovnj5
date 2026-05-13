class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #longest consecutive seq in nums array
        #array isnt sorted
        #return number
        #O(n) runtime

        #createe a set of numbers
        #iterate through list
            #when you get number, see how maney are seuentially after
                #continously until false
                #that would be more than O(n)
                #only do values thta dont have a number lower than it
                #if num-1 in setNums, then skip
                    #else go
        
        setNums = set(nums)

        output = 0

        for num in nums:
            track_seq = 0
            if num-1 in setNums:
                continue
            track_seq += 1
            
            new_num = num+1
           
            while new_num in setNums:
                track_seq += 1
                new_num += 1
            output = max(output, track_seq)
        
        return output

            



        