class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #iterate through nums
        #if target - nums[x] in hashMap
            #return index of hashmap, x
        #else, add to hashmap and iterate
        hashMap = {}
        for x in range(len(nums)):
            if target - nums[x] in hashMap:
                array = [hashMap[target - nums[x]], x]
                return array
            else:
                hashMap[nums[x]] = x