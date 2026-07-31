class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in strs:
            fq = [0] * 26
            for ch in word:
                fq[ord(ch)-ord('a')] += 1
            mp[tuple(fq)].append(word)
        return list(mp.values())