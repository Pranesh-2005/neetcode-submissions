class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row,col = len(image),len(image[0])
        srt = image[sr][sc]
        if srt == color:
            return image
        def dfs(r,c):
            if (r<0 or c<0 or r==row or c==col or image[r][c] != srt):
                return
            image[r][c] = color 
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        dfs(sr,sc)
        return image
        