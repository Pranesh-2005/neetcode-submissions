class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = defaultdict(int)
        for i,ch in enumerate(s):
            mp[ch] = i
        size,end = 0,0
        res = []
        for i,ch in enumerate(s):
            size += 1
            end = max(end,mp[ch])
            if end == i:
                res.append(size)
                size = 0
        return res
