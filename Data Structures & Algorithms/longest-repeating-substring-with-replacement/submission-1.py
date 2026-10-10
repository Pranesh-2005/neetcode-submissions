class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        l,res = 0,0
        maxch = 0
        for r in range(len(s)):
            mp[s[r]] += 1
            maxch = max(maxch,mp[s[r]])
            while r-l+1-maxch > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res