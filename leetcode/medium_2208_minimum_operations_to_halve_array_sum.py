class Solution:
    # Test cases:
    # nums = [] -> 0  # although 1 <= nums.length <= 105
    # nums = [1] -> 1
    # nums = [3,8,20] -> 3
    def halveArray(self, nums: List[int]) -> int:
        # IMPORTANT!!!! BELOW EXPLAINATION EXCEED TIME LIMIT BECAUSE
        # IT KEEPS CALCULATING THE SUM WHICH IS AN ORDER OF N OPERATION.
        # heap = [-1 * num for num in nums]
        # goal = sum(heap) / 2
        # num_ops = 0
        # heapify(heap)
        # while sum(heap) < goal:
        #     num_ops += 1
        #     num = heappop(heap) / 2
        #     heappush(heap, num)
        # return num_ops
    
        heap = [-1 * num for num in nums]
        s = sum(heap)
        goal = s / 2
        num_ops = 0
        heapify(heap)
        while s < goal:
            num_ops += 1
            num = heappop(heap) / 2
            heappush(heap, num)
            s = s - num
        return num_ops
