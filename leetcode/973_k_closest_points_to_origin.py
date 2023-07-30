import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # # Simple 2-liner using sort
        # points.sort(key = lambda P: P[0]**2 + P[1]**2)
        # return points[:K]

        # Intuition
        # Use Heap => closest means min distance to origin
        # max heap pops out large items, heap only keeps k items
        # return the items in the heap when done
        # O(Nlog(K))
        # Test cases:
        # [[0,0]] k=1 -> [[0,0]]
        # [[1,3],[-2,2],[-2,2]], k = 1 -> [[-2,2]]  <= notice I added a dup
        # [[3,3],[5,-1],[-2,4]], k = 2 -> [[3,3],[-2,4]]
        
        heap = []
        for point in points:  # point is a list of [x, y]
            x, y = point
            distance = sqrt(x**2 + y**2)
            heapq.heappush(heap, (-distance, [x, y]))  # what happens on ties???? [2, 1] and [1, 2]
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]  # do not need to sort, but remember to get 2nd item
        

