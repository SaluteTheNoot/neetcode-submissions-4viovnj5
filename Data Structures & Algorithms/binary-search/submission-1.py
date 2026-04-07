class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #sorted array, find particular target value
        #if it does not exist, return -1

        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            value = nums[mid]
            if value < target:
                l = mid + 1
            elif value > target:
                r = mid - 1
            else:
                return mid
        return -1
        