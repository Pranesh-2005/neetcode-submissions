class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols,diag1,diag2 = set(),set(),set()
        position = []
        def backtrack(row):
            if row == n:
                res.append(['.'*c+'Q'+'.'*(n-c-1) for c in position])
                return
            for col in range(n):
                if col in cols or row+col in diag1 or row-col in diag2:
                    continue
                cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)
                position.append(col)
                backtrack(row+1)
                position.pop()
                cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)

        backtrack(0)
        return res