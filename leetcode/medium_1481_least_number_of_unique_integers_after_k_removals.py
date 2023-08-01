from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        heap = []  # we want a min heap here so we can pop off elements with min count
        print(counter)
        # for num, count in enumerate(counter)  <= THIS IS WRONG!!!! enumerate gives an index....
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
        print(heap)
        num_popped = 0
        while len(heap):
            count, num = heapq.heappop(heap)
            num_popped += count
            print(f'popped num={num}, count={count}, num_popped={num_popped}')
            if num_popped > k:
                return len(heap) + 1
            elif num_popped == k:
                return len(heap)

        # we end up with [(2, 1), (3, 3)] after poping (1, 2) and (1, 4)
        # Then we pop (2, 1)
        # if num_popped is 2 + 2 = 4 > k => we popped too much, so we add 1 to result
        # if num_popped is 2 + 1 = 3 == k => we popped exactly all, then what's left is answer
        return 0
