import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Intuition:
        # Note that since question does not care about which project or profit,
        # all we need to do is to return final capital at the end, that's all we need to track.
        # That simplified the algorithm quite a bit.

        # 1 <= n <= 105, n == profits.length == capital.length
        c_and_p = [*zip(capital, profits)]  # ex: [(0, 1), (1, 2), (1, 3)]
        c_and_p.sort()  # sort by capital
        # above could just be one-line:
        # c_and_p = sorted(zip(capital, profits))
        # zip returns <zip object at 0x7f24efa48440>
        heap = []  # max heap
        num_proj = 0
        i = 0  # need a pointer to keep track of profits in a group
        for _ in range(k):
            while i < len(c_and_p) and c_and_p[i][0] <= w:
                heapq.heappush(heap, -c_and_p[i][1])
                i += 1
            if len(heap) == 0:
                return w
            # work on a project
            # w -= c  # THIS IS NOT NEEDED BASED ON THE PROBLEM!
            profit = -heapq.heappop(heap)
            w += profit
        return w

        # # IMPORTANT! BELOW IMPLEMENTATION IS WRONG!!!!
        # # ALL PROFITS WITH THE SAME CAPITAL NEED TO BE PUSHED TOGETHER!!!!
        # for c, p in c_and_p:
        #     if num_proj >= k:
        #         break
        #     heapq.heappush(heap, -p)
        #     if c <= w:
        #         num_proj += 1
        #         w -= c
        #         max_profit = -heapq.heappop(heap)
        #         w += max_profit
        # return w

