class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we know count_zero > 1, return all 0's
        #count_zero = 1, all 0's except where zero is (gets product)
        #count_zero = 0, all are product/nums[i]

        count_zero = 0
        product = 1
        res = [0] * len(nums)
        for num in nums:
            if num:
                product *= num
            else:
                count_zero += 1
        if count_zero > 1:
            return res
        elif count_zero == 1:
            for index, value in enumerate(nums):
                if value:
                    res[index] = 0
                else:
                    res[index] = product
        else:
            for index, value in enumerate(nums):
                res[index]= product//value
        return res

        