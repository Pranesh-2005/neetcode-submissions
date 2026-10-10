class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        mps,mpt = defaultdict(int),defaultdict(int)
        for i in range(len(t)):
            mpt[t[i]] += 1
        res,resL = [-1,-1],float("inf")
        having,needed,l=0,len(mpt),0
        for r in range(len(s)):
            mps[s[r]] += 1
            if s[r] in mpt and mps[s[r]] == mpt[s[r]]:
                having += 1
            while having == needed:
                if r-l+1<resL:
                    resL = r-l+1
                    res = [l,r]
                mps[s[l]] -= 1
                if s[l] in mpt and mps[s[l]] < mpt[s[l]]:
                    having -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resL != float("inf") else "" 