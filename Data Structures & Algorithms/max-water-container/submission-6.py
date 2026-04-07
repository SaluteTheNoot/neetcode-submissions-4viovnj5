class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #need to get max water between two bars of height[i] length
        #do this with two pointers, where the pointer of lower value iterates
        #store max area in var maxVal every time
            #calculate by min(l,r) * distance
        #do while l<r, after return maxVal
        l,r = 0, len(heights)-1
        maxVal = 0
        largest = max(heights)
        while l <= r:
            distance = r - l
            area = distance * min(heights[l], heights[r])
            maxVal = max(maxVal,area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxVal