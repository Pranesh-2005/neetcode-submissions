class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for word in strs:
            fq = [0]*26
            for ch in word:
                fq[ord(ch)-ord('a')] += 1
            grp[tuple(fq)].append(word)
        return list(grp.values())