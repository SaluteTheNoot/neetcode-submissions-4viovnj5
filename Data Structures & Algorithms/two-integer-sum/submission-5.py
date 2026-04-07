class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for x in range(len(nums)):
            find = target - nums[x]
            if find in hashMap:
                output = [hashMap[find],x]
                return output
            else:
                hashMap[nums[x]] = x
        


        