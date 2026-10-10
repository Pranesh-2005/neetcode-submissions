class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)
        res = r
        def canShip(cap):
            curcap = cap
            shp = 1
            for weight in weights:
                if curcap - weight < 0:
                    curcap = cap
                    shp += 1
                curcap -= weight
            return shp<=days
        while l<=r:
            m = l+(r-l)//2
            if canShip(m):
                res=min(res,m)
                r = m-1
            else:
                l = m+1
        return res