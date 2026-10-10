class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        fq = [0]*26
        for ch in s:
            fq[ord(ch)-ord('a')] += 1
        for ch in t:
            fq[ord(ch)-ord('a')] -= 1
        for num in fq:
            if num != 0:
                return False
        return True