class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbor = defaultdict(list)
        wordList.append(beginWord)
        res = 1
        q = deque([beginWord])
        visit = set([beginWord])
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                neighbor[pattern].append(word)
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for neighborword in neighbor[pattern]:
                        if neighborword not in visit:
                            q.append(neighborword)
                            visit.add(neighborword)
            res += 1
        return 0