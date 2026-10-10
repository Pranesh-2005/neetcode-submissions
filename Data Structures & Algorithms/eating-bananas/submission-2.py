class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,sum(piles)
        res = r
        while l<=r:
            m = l+(r-l)//2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/m)
            if hrs<=h:
                res = min(res,m)
                r = m-1
            else:
                l = m+1
        return res