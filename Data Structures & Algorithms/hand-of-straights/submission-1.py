class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        mp = defaultdict(int)
        for num in hand:
            mp[num] += 1
        heap = list(mp.keys())
        heapq.heapify(heap)
        while heap:
            first = heap[0]
            for i in range(first,first+groupSize):
                if i not in mp:
                    return False
                mp[i] -= 1
                if mp[i]==0:
                    if i!=heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
            
                