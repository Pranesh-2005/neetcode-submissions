class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        minp = nums[0]
        for num in nums:
            minp = min(minp,num)
            profit = max(profit,num-minp)
        return profit
        