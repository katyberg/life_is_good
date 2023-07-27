import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Ituition:
        # This is actually very similar to "2208. Minimum Operations to Halve Array Sum"....
        # If we store piles in max heap, each time we pick the heaviest pile and remove half
        # runtime O(N + klogN), space O(N)
        p = [-pile for pile in piles]
        heapq.heapify(p)
        for i in range(k):
            pile = -1 * heapq.heappop(p)
            new_pile = pile - floor(pile / 2)
            heapq.heappush(p, -new_pile)
        return -sum(p)

