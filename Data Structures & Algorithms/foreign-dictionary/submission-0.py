class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        mp = {ch:set() for word in words for ch in word}
        for i in range(len(words) - 1):
            word1,word2 = words[i], words[i+1]
            minlen = min(len(word1),len(word2))
            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ""
            for j in range(minlen):
                if word1[j] != word2[j]:
                    mp[word1[j]].add(word2[j])
                    break
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in mp[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        for c in mp:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
