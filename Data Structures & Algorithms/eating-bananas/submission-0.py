class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:
        l,r = 1,max(nums)
        res = r
        while l<=r:
            hrs = 0
            k = (l +r)// 2
            for num in nums:
                hrs += math.ceil(num/k)
            if hrs <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1
        return res