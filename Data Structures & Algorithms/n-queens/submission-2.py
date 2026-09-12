class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols,diag1,diag2 = set(),set(),set()
        placement = []
        def dfs(row):
            if row == n:
                res.append(['.'*c+'Q'+'.'*(n-c-1) for c in placement])
                return
            for col in range(n):
                if col in cols or row+col in diag1 or row-col in diag2:
                    continue
                cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)
                placement.append(col)
                dfs(row+1)
                placement.pop()
                cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)

        dfs(0)
        return res