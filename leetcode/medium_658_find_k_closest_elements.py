import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # This is a heap solution
        heap = []
        for num in arr:
            heapq.heappush(heap, (-abs(num - x), -num))  # notice - <= max heap
            # if there are ties, 2nd element will be used to compare,
            # so (-5, -15) will be popped earlier than (-5, -3) which is what we want.
            if len(heap) > k:
                heapq.heappop(heap)
        result = [-item[1] for item in heap]
        result.sort()  # return in ascending order 
        return result
    
        # # Btw could just be two-lines
        # # Funny this has the fastest runtime.... >_<
        # sorted_arr = sorted(arr, key = lambda num: abs(x - num))
        # return sorted(sorted_arr[:k])

