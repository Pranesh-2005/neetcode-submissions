class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pat = defaultdict(list)
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                pat[pattern].append(word)
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for wrd in pat[pattern]:
                        if wrd not in visit:
                            visit.add(wrd)
                            q.append(wrd)
            res += 1
        return 0
