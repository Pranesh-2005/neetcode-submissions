class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.hsrb1(nums[1:]),self.hsrb1(nums[:-1]))
        
    def hsrb1(self,nums):
        rob1,rob2 = 0,0
        for num in nums:
            rob = max(num+rob1,rob2)
            rob1 = rob2
            rob2 = rob
        return rob2