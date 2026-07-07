import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # create max heap
        heap = []

        res = []

        # add to the heap
        for point in points:
            point_distance = point[0]**2 + point[1]**2
            if len(heap) < k:
                heapq.heappush(heap, (-(point_distance), point))
            
            # else if the new point is closer (less than farthest distance)
            elif -(heap[0][0]) > point_distance:
                heapq.heappop(heap)
                heapq.heappush(heap, (-(point_distance), point))
        
        for point in heap:
            res.append(point[1])
        
        return res