class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        l = 0
        mxL = 0
        res = 0
        for r in range(len(s)):
            mp[s[r]] += 1
            mxL = max(mxL,mp[s[r]])
            while r - l + 1 - mxL > k:
                mp[s[l]] -= 1
                l += 1
            res = max(mxL,r-l+1)
        return res
                                