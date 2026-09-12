class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path,opens,closes):
            if len(path)==2*n:
                res.append(''.join(path))
                return
            if opens < n:
                path.append('(')
                backtrack(path,opens+1,closes)
                path.pop()
            if closes < opens:
                path.append(')')
                backtrack(path,opens,closes+1)
                path.pop()

        backtrack([],0,0)
        return res