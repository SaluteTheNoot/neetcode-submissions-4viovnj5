class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #return index (1 indexxed) of two numbers that add to target
            #array is sorted in non-decreasing order  
            # only one valid solution, index1 and index2 will not be ==     
        #solution must use O(1) space
        #use pointers

        #while l < r:
            #if num[l] + num[r] < target:
                #l += 1
            #elif num[l] + num[r] > target:
                #r -= 1
            #else:
                #return [l+1,r+1]
        
        l,r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l+1,r+1]
        