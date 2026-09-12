class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patmap = defaultdict(list)
        wordList.append(endWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                patmap[pattern].append(word)
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
                    for neiword in patmap[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res += 1
        return 0
