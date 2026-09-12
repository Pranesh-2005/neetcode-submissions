class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start,path):
            if start == len(s):
                res.append(path[:])
            for end in range(start+1,len(s)+1):
                p = s[start:end]
                if p == p[::-1]:
                    path.append(p)
                    backtrack(end,path)
                    path.pop()
        backtrack(0,[])
        return res
        