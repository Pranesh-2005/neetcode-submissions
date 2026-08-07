class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b, '*': lambda a,b: a*b, '/': lambda a,b: int(a/b)}
        for ch in tokens:
            if ch in ops:
                b,a = stk.pop(),stk.pop()
                stk.append(ops[ch](a,b))
            else:
                stk.append(int(ch))
        return stk[-1]
        