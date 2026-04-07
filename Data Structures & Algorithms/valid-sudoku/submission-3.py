class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashRow = defaultdict(list)
        hashCol = defaultdict(list)
        hashThree = defaultdict(list)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in hashRow[r] or board[r][c] in hashCol[c] or board[r][c] in hashThree[r//3, c//3]:
                    return False
                else:
                    hashRow[r].append(board[r][c])
                    hashCol[c].append(board[r][c])
                    hashThree[r//3,c//3].append(board[r][c])
        return True
        