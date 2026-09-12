class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            sq = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap,(-sq,point))
            while len(heap) > k:
                heapq.heappop(heap)
        return [point for _,point in heap]