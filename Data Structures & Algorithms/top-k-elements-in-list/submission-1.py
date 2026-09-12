class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        heap = []
        for num,frq in mp.items():
            heapq.heappush(heap,(frq,num))
            while len(heap) > k:
                heapq.heappop(heap)
        return [num for _,num in heap]