class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        stk = []
        for i,num in enumerate(nums):
            while stk and nums[stk[-1]]<num:
                ind = stk.pop()
                res[ind]=i-ind
            stk.append(i)
        return res
        