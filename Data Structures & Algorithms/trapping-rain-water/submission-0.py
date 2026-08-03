class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height)-1
        lmx,rmx = height[l],height[r]
        while l<r:
            if lmx < rmx:
                l += 1
                lmx = max(lmx,height[l])
                res += lmx - height[l]
            else:
                r -= 1
                rmx = max(rmx,height[r])
                res += rmx - height[r]
        return res

        