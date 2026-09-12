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
        res,visited = set(),set()
        row,col = len(board),len(board[0])
        def dfs(r,c,node,word):
            if (r<0 or c<0 or (r,c) in visited or r==row or c == col or board[r][c] not in node.children):
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            visited.remove((r,c))        
        
        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        return list(res)
        

        