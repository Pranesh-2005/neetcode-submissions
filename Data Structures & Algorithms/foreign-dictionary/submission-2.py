class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        mp = {ch:set() for word in words for ch in word}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    mp[w1[j]].add(w2[j])
                    break
        res = []
        visit = {}
        def dfs(ch):
            if ch in visit:
                return visit[ch]
            visit[ch] = True
            for nei in mp[ch]:
                if dfs(nei):
                    return True
            visit[ch] = False
            res.append(ch)
        for ch in mp:
            if dfs(ch):
                return ""
        res.reverse()
        return "".join(res)