class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #a 2d matrix, sorted in non-decreasing order
            #number only gets larger as yiuo continue to iterate
        l,r = 0, len(matrix)-1
        #while loop, when suitable array found then break
        while l <= r:
            m = (l+r)//2
            if target > matrix[m][-1]:
                l = m+1
            elif target < matrix[m][0]:
                r = m-1
            else:
                break
        if not (l <= r):
            return False

        newList = matrix[m]
        l,r = 0, len(newList)-1
        while l <= r:
            m = (l+r)//2
            if target > newList[m]:
                l = m+1
            elif target < newList[m]:
                r = m-1
            elif target == newList[m]:
                return True
        return False

        