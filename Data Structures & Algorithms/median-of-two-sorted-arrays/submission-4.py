class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2
        total = len(a)+len(b)
        half = total//2
        if len(b)<len(a):
            a,b = b,a
        l,r = 0,len(a)-1
        while True:
            i = l+(r-l)//2
            j = half-i-2
            aleft = a[i] if i>=0 else float("-inf")
            aright = a[i+1] if (i+1)<len(a) else float("inf")
            bleft = b[j] if j>=0 else float("-inf")
            bright = b[j+1] if (j+1)<len(b) else float("inf")
            if aleft <= bright and bleft <= aright:
                if total%2:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft)+min(aright,bright)) / 2
            if aleft < bright:
                l = i+1
            else:
                r = i-1
        