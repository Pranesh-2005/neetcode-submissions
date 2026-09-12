class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            fst = heapq.heappop(stones)
            scnd = heapq.heappop(stones)
            if scnd > fst:
                heapq.heappush(stones,fst-scnd)
        stones.append(0)
        return abs(stones[0])
        