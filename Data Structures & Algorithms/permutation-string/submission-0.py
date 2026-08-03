class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        mps1,mps2 = defaultdict(int),defaultdict(int)
        for i in range(len(s1)):
            mps1[s1[i]] += 1
            mps2[s2[i]] += 1
        if mps1==mps2: return True
        for r in range(len(s1),len(s2)):
            mps2[s2[r]] += 1
            l = s2[r-len(s1)]
            mps2[l] -= 1
            if mps2[l] == 0:
                del mps2[l]
            if mps1 == mps2:
                return True
        return False
        