class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            distance = p[0] ** 2 + p[1] ** 2
            heapq.heappush(heap,(-distance,p))
            if len(heap) > k:
                heapq.heappop(heap)
        return [p for _,p in heap]
        