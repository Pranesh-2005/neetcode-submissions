class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        minval = min(val,self.stk[-1][1] if self.stk else val)
        self.stk.append((val,minval))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
