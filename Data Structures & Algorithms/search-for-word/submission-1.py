class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        def backtrack(i,r,c):
            if i == len(word):
                return True
            if not (0<=r<row and 0<=c<col) or board[r][c] != word[i]:
                return False
            board[r][c] = '#'
            found = (backtrack(i+1,r+1,c) or backtrack(i+1,r-1,c) or backtrack(i+1,r,c+1) or backtrack(i+1,r,c-1))
            board[r][c] = word[i]
            return found
        for r in range(row):
            for c in range(col):
                if backtrack(0,r,c):
                    return True
        return False