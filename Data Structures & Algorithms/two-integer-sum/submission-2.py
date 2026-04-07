class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x in range(len(nums)):
            find = target - nums[x]
            if find in hashmap:
                return hashmap[find],x
            else:
                hashmap[nums[x]] = x
