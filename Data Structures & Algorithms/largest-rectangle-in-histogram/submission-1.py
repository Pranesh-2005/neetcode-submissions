class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stk = []
        for i,height in enumerate(heights):
            st = i
            while stk and stk[-1][0] > height:
                hei,ind = stk.pop()
                res = max(res,hei*(i-ind))
                st = ind
            stk.append((height,st))
        for height,i in stk:
            res = max(res,height*(len(heights)-i))
        return res
        