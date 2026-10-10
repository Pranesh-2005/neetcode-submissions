class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for i,ch in enumerate(s):
            mp[ch] = i
        res = []
        end,size = 0,0
        for i,ch in enumerate(s):
            size += 1
            end = max(end,mp[ch])
            if i == end:
                res.append(size)
                size = 0
        return res