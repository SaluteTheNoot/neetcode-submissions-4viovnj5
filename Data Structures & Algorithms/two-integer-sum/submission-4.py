class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for x in range(len(nums)):
            if target - nums[x] in hashMap:
                chungus = [hashMap[target - nums[x]], x]
                return chungus
            else:
                hashMap[nums[x]] = x