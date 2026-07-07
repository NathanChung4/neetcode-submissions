import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.K = k
        for num in nums:
            kth = self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.K:
            heapq.heappush(self.heap,val)
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        
        return self.heap[0]

