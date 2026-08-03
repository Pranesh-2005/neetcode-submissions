class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        mpT,mpS = defaultdict(int),defaultdict(int)
        for ch in t:
            mpT[ch] += 1
        hv,nd = 0,len(mpT)
        res,resL = [-1,-1],float("inf")
        l = 0
        for r in range(len(s)):
            mpS[s[r]] += 1
            if s[r] in mpT and mpS[s[r]] == mpT[s[r]]:
                hv += 1
            while hv == nd:
                if (r-l+1) < resL:
                    res = [l,r]
                    resL = r-l+1
                mpS[s[l]] -= 1
                if s[l] in mpT and mpS[s[l]] < mpT[s[l]]:
                    hv -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resL != float("inf") else ""
