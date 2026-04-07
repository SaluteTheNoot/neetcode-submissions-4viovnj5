class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #given array of ints nums and int target
        #return index I and J where nums[I] + nums[J] == target and I != J
        #every input has a solution, so you dont need to worry about that

        #you can easily use two pointers for O(n^2)
        
        """for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    if i < j:
                        return [i,j] #smallest first so deal with that later
                    else:
                        return [j,i]*
                        """
        #we can do this in less than that at O(n) tho using a hashmap to keep track of values

        hashMap = {}

        for index, num in enumerate(nums):

            find = target - num

            if find in hashMap:
                index1 = hashMap[find]
                return [index1, index]
            
            hashMap[num] = index




        