class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastind = {}
        for i,ch in enumerate(s):
            lastind[ch] = i
        res = []
        size,end = 0,0
        for i,ch in enumerate(s):
            size += 1
            end = max(end,lastind[ch])
            if i == end:
                res.append(size)
                size = 0
        return res