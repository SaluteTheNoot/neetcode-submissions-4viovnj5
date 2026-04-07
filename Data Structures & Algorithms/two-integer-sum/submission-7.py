class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for x,y in enumerate(nums):
            find = target - y
            if find in hashMap:
                return [hashMap[find], x]
            else:
                hashMap[y] = x

        