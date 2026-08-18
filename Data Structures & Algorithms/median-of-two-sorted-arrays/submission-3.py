class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(b) < len(a):
            a,b = b,a
        l,r = 0,len(a)-1
        while True:
            i = (l+r) // 2
            j = half - i - 2
            alft = a[i] if i>=0 else float("-inf")
            arig = a[i+1] if (i+1) < len(a) else float("inf")
            blft = b[j] if j >= 0 else float("-inf")
            brig = b[j+1] if (j+1) < len(b) else float("inf")
            if alft <= brig and blft <= arig:
                if total % 2:
                    return min(arig,brig)
                return (max(alft,blft) + min(arig,brig)) / 2
            elif alft < brig:
                l = i + 1
            else:
                r = i - 1
        