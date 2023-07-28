import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Intuition:
        # Easy approach - sort the array get kth elements from the end => O(NlogN)
        # Better approach - "largest" => think of heap
        # use min heap with at most k elements (pop off min as I go),
        # the top of the heap at the end IS the kth largest element!
        # => O((N+K)*logK)
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        # top element is the kth largest (smallest in min heap with k elelments)
        return heap[0]  # 1 <= k <= nums.length <= 105

        # # Below is my solution using Counter in the past (practice in Apple Interview)
        # # Build counter for the array
        # from collections import Counter
        # counter = Counter(nums)
        # # Sort counter keys decending
        # # keys_desc = counter.keys.sort(reverse=True)  <== This is wrong!
        # keys_desc = sorted(list(counter), reverse=True)
        # # Start with largest key, calculate sum, if k <= sum, return key
        # count_sum = 0
        # for key in keys_desc:
        #     count_sum += counter[key]
        #     if k <= count_sum:
        #         return key
        

