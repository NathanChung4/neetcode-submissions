import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # need to negate on the way in and out of heap

        heap = []

        # fill the heap with stones
        for s in stones:
            heapq.heappush(heap, -(s))
        
        while len(heap) > 1:
            first = -(heapq.heappop(heap))
            second = -(heapq.heappop(heap))

            if first > second:
                first -= second
                heapq.heappush(heap, -(first))
            
        if not heap:
            return 0
        else:
            return -(heap[0])

