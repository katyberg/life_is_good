import heapq
class KthLargest:
    # Intuition:
    # 1. Sort list after each add => O(NlogN)
    # 2. Binary search tree => O(logN)
    # 3. Heap => O(logN)
    #    - I can make a copy and pop, but that will take too much space
    #    - How about I pop and then push them back. But what if k is very big?
    #    - THE KEY IS TO:
    #      REMOVE ALL ELEMENTS THAT ARE SMALLER THAN KTH LARGEST ELEMENTS!!!!

    # Test cases:
    # It is guaranteed that there will be at least k elements in the array 
    # when you search for the kth element.
    # ["KthLargest", "add", "add", "add", "add", "add"]
    # [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums  # min heap but only keep k elements always
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        # 1 <= k <= 104
        heapq.heappush(self.heap, val)
        n = len(self.heap)
        for i in range(n - self.k):
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
