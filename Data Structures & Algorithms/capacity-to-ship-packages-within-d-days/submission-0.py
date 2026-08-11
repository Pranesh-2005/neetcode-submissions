class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        l,r = max(nums),sum(nums)
        res = r
        def canShip(cap):
            shp,curCap = 1,cap
            for num in nums:
                if curCap - num < 0:
                    shp += 1
                    curCap = cap
                curCap -= num
            return shp <= days
        while l<=r:
            cap = l + (r-l) // 2
            if canShip(cap):
                res = min(res,cap)
                r = cap - 1
            else:
                l = cap + 1
        return res
        