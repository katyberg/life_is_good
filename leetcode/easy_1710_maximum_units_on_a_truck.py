import heapq
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Intuition:
        # I can either sort the list or use heap, I will use heap.
        # 1. Build Max heap, largest number of units on top
        # 2. While loop
        #    - pop off max unit
        #    - Put on truck as many as I can, calculate total units as I go
        # Runtime O(NlogN) + O(N) => O(NlogN)
        heap = []
        # Example: boxTypes = [[1,3],[2,2],[3,1]], box_type = [1,3]
        for box_type in boxTypes:
            num_box, num_units = box_type[0], box_type[1]
            heapq.heappush(heap, (-num_units, num_box))  # -1 because it's max heap
        total_num_boxes = 0
        total_units = 0
        while heap:
            if total_num_boxes >= truckSize:
                break
            num_box_allowed = truckSize - total_num_boxes
            box_type = heapq.heappop(heap)
            num_units, num_box = -box_type[0], box_type[1]  # -1 because it's max heap
            to_load = min(num_box_allowed, num_box)
            total_num_boxes += to_load
            total_units += (to_load * num_units)
        return total_units

