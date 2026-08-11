class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        mxArea = 0
        stk = []
        for i,h in enumerate(nums):
            start = i
            while stk and stk[-1][1] > h:
                ind,hei = stk.pop()
                mxArea = max(mxArea, hei * (i-ind))
                start = ind
            stk.append((start,h))
        for i,h in stk:
            mxArea = max(mxArea, h * (len(nums) - i))
        return mxArea