import heapq

class MedianFinder:

    def __init__(self):
        # min heap is for the top half and max is for bottom
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        # first case when both are empty
        if not self.minHeap and not self.maxHeap:
            heapq.heappush(self.minHeap, num)
            return
        
        if num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -(num))

        # size balancing
        if len(self.minHeap) - len(self.maxHeap) > 1:
            minPop = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -(minPop))
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            maxPop = -(heapq.heappop(self.maxHeap))
            heapq.heappush(self.minHeap, maxPop)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -(self.maxHeap[0])) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -(self.maxHeap[0])


        