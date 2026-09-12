class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def addWord(self,word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        rows,cols = len(board),len(board[0])
        visited,res = set(),set()
        def dfs(r,c,cur,word):
            if (r<0 or c<0 or r==rows or c==cols or (r,c) in visited or board[r][c] not in cur.children):
                return
            visited.add((r,c))
            cur = cur.children[board[r][c]]
            word += board[r][c]
            if cur.end:
                res.add(word)
            dfs(r-1,c,cur,word)
            dfs(r+1,c,cur,word)
            dfs(r,c-1,cur,word)
            dfs(r,c+1,cur,word)
            visited.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)
        