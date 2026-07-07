import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        maxHeap, minHeap = [], []
        taskCounter = {}
        t = 0

        for task in tasks:
            if task in taskCounter:
                taskCounter[task] += 1
            else:
                taskCounter[task] = 1

        for value in taskCounter.values():
            heapq.heappush(maxHeap, (-(value)))
        
        while maxHeap or minHeap:
            if minHeap:
                while minHeap and minHeap[0][0] <= t:
                    minPop = heapq.heappop(minHeap)
                    heapq.heappush(maxHeap, (-(minPop[1])))

            if not maxHeap:
                t += 1
                continue

            maxPop = -(heapq.heappop(maxHeap))
            if maxPop > 1:
                heapq.heappush(minHeap, ((t+n+1), (maxPop - 1)))
                
            t += 1
        
        return t

            