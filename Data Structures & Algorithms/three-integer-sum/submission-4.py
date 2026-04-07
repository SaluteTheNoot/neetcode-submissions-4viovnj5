from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new = sorted(nums)
        output = []
        for x in range(len(new) - 2):
            if x > 0 and new[x] == new[x - 1]:
                continue
            for y in range(x + 1, len(new) - 1):
                if y > x + 1 and new[y] == new[y - 1]:
                    continue
                for z in range(y + 1, len(new)):
                    if z > y + 1 and new[z] == new[z - 1]:
                        continue
                    elif new[x] + new[y] + new[z] == 0:
                        output.append([new[x], new[y], new[z]])
        return output
