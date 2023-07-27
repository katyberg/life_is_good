import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total_cost = 0
        while len(sticks) > 1:  # 1 <= sticks.length <= 104
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            cost = stick1 + stick2
            total_cost += cost
            heapq.heappush(sticks, cost)
        return total_cost

