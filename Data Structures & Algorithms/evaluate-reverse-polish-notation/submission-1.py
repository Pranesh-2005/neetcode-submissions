class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        mp = {'+': lambda a,b: a+b, '-': lambda a,b:a-b, '*': lambda a,b: a*b, '/': lambda a,b: int(a/b)}
        for ch in tokens:
            if ch in mp:
                b,a = stk.pop(),stk.pop()
                stk.append(mp[ch](a,b))
            else:
                stk.append(int(ch))
        return stk[-1]
