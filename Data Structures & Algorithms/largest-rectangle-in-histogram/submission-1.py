class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for x in range(0,len(heights)):
            newArea = heights[x]
            left = False
            right = False
            leftVal = x-1
            rightVal = x+1
            while left == False:
                if leftVal < 0:
                    left = True
                elif heights[leftVal] >= heights[x]:
                    newArea += heights[x]
                    leftVal -= 1
                else:
                    left = True

            while right == False:
                if rightVal > len(heights)-1:
                    right = True
                elif heights[rightVal] >= heights[x]:
                    newArea += heights[x]
                    rightVal += 1
                else:
                    right = True
            maxArea = max(maxArea, newArea)
        return maxArea
        