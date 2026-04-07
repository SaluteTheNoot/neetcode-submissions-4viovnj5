from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check if sudoku board has duplicates
            #across rows, columns, and 3x3 sub boxes
            #do not need to be solvable to be valid
            #return True if valid, else False
        

        #must be able to store and then check info for:
            #rows
            #columns
            #3 by 3 squares
        
        #can be done with a hashMap, easily store and check information

        row = defaultdict(list)
        col = defaultdict(list)
        three = defaultdict(list)

        for r in range(9):
            for c in range(9):
                
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in three[r//3,c//3]:
                    return False
                else:
                    row[r].append(board[r][c])
                    col[c].append(board[r][c])
                    three[r//3,c//3].append(board[r][c])
        return True

