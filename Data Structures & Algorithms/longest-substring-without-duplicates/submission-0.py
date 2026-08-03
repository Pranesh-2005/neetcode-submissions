class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            mp[s[r]] += 1
            while mp[s[r]] > 1:
                mp[s[l]] -=1
                l += 1
            res = max(res,r-l+1)
        return res