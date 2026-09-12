class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        for task in tasks:
            mp[task] += 1
        count = mp.values()
        maxFreq = max(count)
        tied = sum(c == maxFreq for c in count)
        time = (maxFreq - 1) * (n+1)+tied
        return max(len(tasks),time)