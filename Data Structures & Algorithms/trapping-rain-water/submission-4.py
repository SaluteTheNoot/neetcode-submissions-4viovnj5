class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l,r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        output = 0
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                output += maxl - height[l]
            elif maxl >= maxr:
                r -= 1
                maxr = max(maxr, height[r])
                output += maxr - height[r]
        return output



        