class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        #need to check that each row has no duplicates
        #need to check that each col has no duplicates
        #need to check each 3x3 grid has no duplicates

        row = defaultdict(set)
        col = defaultdict(set)
        three = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in three[(r//3,c//3)]:
                    return False
                
                row[r].add(board[r][c])
                
                col[c].add(board[r][c])
                
                three[(r//3,c//3)].add(board[r][c])


        return True
        