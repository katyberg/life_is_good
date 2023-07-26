import heapq
class MedianFinder:
    # IMPORTANT: READ THIS AGAIN:
    # https://leetcode.com/problems/find-median-from-data-stream/editorial/

    # IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # REMEMBER TO -1 ALL ELEMENTS IN MAX_HEAP BECAUSE HEAPQ IS ONLY FOR MIN_HEAP!!!!

    # Inutition:
    # Brute force:
    # 1. store in resizable array, quicksort when retrieve median: 
    #    add O(1), sort O(NlogN) and return middle O(1)
    #    => runtime O(NlogN), space O(N)
    # 2. insertion sort into sorted array => O(N^2), space O(N)
    # 3. since list is sorted, binary search and then insert
    #    => O(logN) + O(N) shift elements out => O(N)
    # Pop quiz: Can we use a linear search instead of a binary search to find insertion position, without incurring any significant runtime penalty????
    # (Bucket sort I think.... There is also Reservoir Sampling)
    # 4. Two heaps
    #    log(N) for insertion, O(1) for findMedian
    #    Thinking:
    #        1. Don't need to sort everything!!!!
    #        2. Maintain direct access to median element
    #        3. fast way to insert each element
    # 5. Binary Search Tree

    # Test cases:
    # [] => There will be at least one element in the data structure before calling findMedian.
    # [1] => 1
    # [1,2] => 1.5
    # [1,2,3] => 2
    # [1,3,7,13,36,100] => 10
    def __init__(self):
        # We use max_heap and min_heap to store N elements.
        # At all time, max_heap can have at most one more element than min_heap.
        # When n (total number of elements) is odd, max_heap will have exactly 1 more
        # element than min_heap. Otherwise they have the same number of elements.
        # max_heap will contain the one extra element if n is odd
        self.max_heap = []  # has at most 1 more element than min_heap
        self.min_heap = []
        # Apparently below is not needed....
        # heapq.heapify(self.max_heap)
        # heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        # When we get a new num, we follow these procedures:
        # The important point is we want the new number to go through both heaps,
        # so that it is put in the right place, then we balance the numbers!
        # 1. add to max_heap
        # 2. pop max_heap, add to min_heap
        # 3. balance number of two heaps, max_heap can have at most 1 more than min_heap
        heapq.heappush(self.max_heap, -num)
        x = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -x)
        if not (len(self.max_heap) == len(self.min_heap) or
                len(self.max_heap) == len(self.min_heap) + 1):
            y = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -y)

    def findMedian(self) -> float:
        # When n is even, median is the average of max of max_heap and min of min_heap
        # When n is odd, top of max_heap is the median
        # (because in our implementation max_heap contains the extra element in odd case)
        if len(self.max_heap) == len(self.min_heap):
            # at least 1 when findMedian is called, so they must both be 1
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            # at least 1 when findMedian is called
            return -self.max_heap[0]  # when n is odd, top of max_heap is the median
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
