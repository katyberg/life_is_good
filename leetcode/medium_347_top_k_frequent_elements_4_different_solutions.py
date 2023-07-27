from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # See https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/708/heaps/4641/
        # Let's implement this problem in two different ways:
        # 1. Hash Map then sort => O(NlogN)
        # 2. Hash Map then heap => O(NlogK)
        # 3. Bucket sort => O(N)  <- this problem has bound domain so it's applicable.

        # # Implementation 1: Hash Map then sort => O(NlogN)
        # 
        # # 1a: Just use counter and sorting
        # counter = Counter(nums)
        # s = sorted(counter.items(), key=lambda pair: pair[1], reverse=True)[:k]
        # # ps: sorted counter.items() are like this [(1, 3), (2, 2), (3, 1)]
        # # counter=Counter({1: 3, 2: 2, 3: 1}), s=[(1, 3), (2, 2)]
        # return list(map(lambda pair: pair[0], s))
        #
        # # 1b: Use counter builtin function most_common
        # # counter.most_common() is like this [(1, 3), (2, 2), (3, 1)]
        # counter = Counter(nums)
        # return list(map(lambda pair: pair[0], counter.most_common(k)))
        # # or
        # # return [entry[0] for entry in counter.most_common(k)]
        # # return [key for key, val in counter.most_common(k)]

        # Implementation 2: Hash Map then heap => O(NlogK)
        # Because k is in the range [1, the number of unique elements in the array]
        # slight optimization to make sure we don't become O(NlogN)....
        if k == len(nums):
            return nums
        counter = Counter(nums)  # {1: 3, 2: 2, 3: 1}
        count_num = [(count, num) for num, count in counter.items()]
        # count_num is like [(3, 1), (2, 2), (1, 3)]
        heap = []  # we want min heap pop when len exceeds k
        for item in count_num:
            heapq.heappush(heap, item)  # (3, 1), (2, 2), (1, 3)
            if len(heap) > k:
                heapq.heappop(heap)  # pop (1, 3)
        return [num for count, num in heap]
        # # The above steps can be squished into ONE LINE (as usual)!!!!
        # return heapq.nlargest(k, counter.keys(), key=counter.get)

        # # Ps: above we can just do:
        # for key, val in counts.items():
        #     heapq.heappush(heap, (val, key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # # Implementation 3: Bucket sort => O(N)
        # counter = Counter(nums)  # ex: {1:3, 2:2, 3:1, 4:2}
        # buckets = [[]] * len(nums)  # ex: [[],[],[],....] NOTE [[]] NOT []
        # for num, count in counter.items():
        #     buckets[count-1].append(num)  # ex: [[3],[2,4],[1],....]
        # result = []
        # for bucket in reversed(buckets):  # reversed is faster than [::-1]
        #     result.append(*bucket)  # [1,2,4,3...] k=3
        #     if len(result) >= k:
        #         break
        # return result[:k]
     
