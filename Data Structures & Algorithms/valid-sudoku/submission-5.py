from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check if the Sudoku board is valid by row, col and sub box
        
        #we want to check if each row has any duplicates, how would we do this?
        #we can iterate throughout the row, continue adding items
            #if there is a duplicate, then invalid
            #use a dictionary to get this done
        #while going through the rows, we can also check the cols at the same time
        #to check the sub-boxes ...
            #a subox is determined by dividing (//) x and y coordinate by 3
            #use dictionary as well just like the other row and col
        
        #skip over the "." parts of the board, they are not relevant

        row = defaultdict(set)
        col = defaultdict(set)
        three = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in three[(r//3, c//3)]:
                    return False
                else:
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    three[(r//3, c//3)].add(board[r][c])
        return True

                