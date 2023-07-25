import heapq
class Solution:
    # Test cases:
    # stones = [] -> 0  # but actually 1 <= stones.length <= 30
    # stones = [1] -> 1
    # stones = [1,2] -> 1
    # stones = [2,2] -> 0
    # stones = [1,2,3] -> 0

    # Runtime O(NlogN), Space O(N)

    def lastStoneWeight(self, stones: List[int]) -> int:
        # We need to reverse sign of all stones to use heapq so it acts as maxheap.

        # IMPORTANT!!!! BELOW USAGE OF heapq IS WRONG!!!!
        # stones_sign_reversed = [-1 * stone for stone in stones]
        # heap = heapify(stones_sign_reversed)

        heap = [-1 * stone for stone in stones]
        heapify(heap)
        while len(heap):
            if len(heap) == 1:
                return -1 * heap[0]
            x = heappop(heap)
            y = heappop(heap)
            diff = abs(x - y)
            if diff == 0:
                continue
            else:
                # heappush(-1 * diff)  # IMPORTANT! NEED TO PASS IN heap to heappush!!!!
                heappush(heap, -1 * diff)
        return 0
