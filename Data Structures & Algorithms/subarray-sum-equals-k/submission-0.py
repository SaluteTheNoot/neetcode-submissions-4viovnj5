class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = currsum = 0

        hashMap = {0:1}


        for num in nums:
            currsum += num

            total = currsum - k

            result += hashMap.get(total,0)

            hashMap[currsum] = hashMap.get(currsum,0) + 1
            




        return result
        