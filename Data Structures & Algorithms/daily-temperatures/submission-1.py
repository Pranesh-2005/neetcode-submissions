class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        stk = []
        for i in range(len(nums)):
            while stk and nums[stk[-1]] < nums[i]:
                ind = stk.pop()
                res[ind] = i - ind
            stk.append(i)
        return res