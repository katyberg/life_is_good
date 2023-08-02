from collections import Counter
import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Intuition:
        # remove integer with max amount of repeatition each time
        # until there is no more distinct integer left
        # use max heap, key is the count
        # build counter first to give the count
        
        heap = []  # max heap
        counter = Counter(arr)  # arr = [3,3,3,3,5,5,5,2,2,7] => {3:4, 5:3, 2:2, 7:1}
        for count in counter.values():
            heapq.heappush(heap, -count)  # - because of max heap
        new_size = len(arr)
        half_size = len(arr) // 2  # arr.length is even
        to_remove = 0
        while heap:
            if new_size <= half_size:
                break
            count = -heapq.heappop(heap)
            new_size -= count  # - because of max heap
            to_remove += 1
        return to_remove

        # # Btw, counter provides most_common function already
        # # In Python, we can use the built-in Counter class for multi-set.
        # counts = collections.Counter(arr)
        # # Extract the counts in reverse-sorted order.
        # # most_common gives (number, count) pairs, reverse sorted on count.
        # counts = [count for number, count in counts.most_common()]

