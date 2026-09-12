class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        fresh,time = 0,0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r>0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    q.append([r-1,c])
                    fresh -= 1
                if r<rows-1 and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    q.append([r+1,c])
                    fresh -= 1
                if c>0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    q.append([r,c-1])
                    fresh -= 1
                if c<cols-1 and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    q.append([r,c+1])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1