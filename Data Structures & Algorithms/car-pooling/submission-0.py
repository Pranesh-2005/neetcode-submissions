class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        heap = []
        curpass = 0
        for t in trips:
            numpass,start,end = t
            while heap and heap[0][0] <= start:
                curpass -= heap[0][1]
                heapq.heappop(heap)
            curpass += numpass
            heapq.heappush(heap,(end,numpass))
            if curpass > capacity:
                return False
        return True