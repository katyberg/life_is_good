import heapq
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        # Intuition:
        # This is basically the same question as
        # https://leetcode.com/problems/maximum-units-on-a-truck/description/
        # I like to use heap (priority queue)
        # To fit max number of apples, I need to pick small apples first,
        # so I will use min heap to store the apples.

        heap = []
        for apple_weight in weight:
            heapq.heappush(heap, apple_weight)  # min heap
        weight_limit = 5000
        total_weight = 0
        total_num_apple = 0
        while heap:
            apple_weight = heapq.heappop(heap)
            # NOTICE NOT >= ex: [1000,1000,1000,1000,1000]
            if total_weight + apple_weight > weight_limit:
                break
            else:
                total_weight += apple_weight
                total_num_apple += 1
        return total_num_apple
