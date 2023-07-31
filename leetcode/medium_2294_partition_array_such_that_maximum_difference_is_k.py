class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_num_subseq = 1
        subseq_begin = nums[0]
        upper_bound = subseq_begin + k
        for i, num in enumerate(nums):
            if num > upper_bound:
                subseq_begin = nums[i]
                upper_bound = num + k
                min_num_subseq += 1
        return min_num_subseq
        
        # # This is more succint
        # nums.sort()
        # ans = 1
        # x = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] - x > k:
        #         x = nums[i]
        #         ans += 1
        # return ans
