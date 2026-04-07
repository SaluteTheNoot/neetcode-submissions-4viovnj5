class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        l = 0
        r = len(matrix[0])-1
        search = []

        while top <= bottom:
            mid = (top+bottom)//2
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bottom = mid-1
            else:
                break

        if not (top <= bottom):
            return False
        
        row = matrix[mid]
        l = 0
        r = len(row) - 1
        
        while l <= r:
            middle = (l + r) // 2
            if target > row[middle]:
                l = middle + 1
            elif target < row[middle]:
                r = middle - 1
            else:
                return True
        
        return False
