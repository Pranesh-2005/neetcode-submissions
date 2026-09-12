class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(opens,closes,path):
            if len(path) == 2*n:
                res.append(''.join(path))
                return
            if opens<n:
                path.append('(')
                backtrack(opens+1,closes,path)
                path.pop()
            if closes < opens:
                path.append(')')
                backtrack(opens,closes+1,path)
                path.pop()
        backtrack(0,0,[])
        return res
        