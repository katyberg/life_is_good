class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Ituition:
        # This problem is not super intuitive....
        # It is also not too obvious what the DP part is....
        # But I was able to figure it out....

        # DP:
        # The longest increasing subsequence (LIS) for every subarray ending at index i
        # is the max between initial value (which is 1) and 1 + dp(j), j is [0, i) AND
        # j is between index 0 to i - 1 where nums[j] is SMALLER THAN nums[i].
        # In other words, the LIS at index i is one more than the LIS of each index before it
        # plus 1 that has a value smaller than the value at index i.
        # MEMORIZATION STATE => THE LIS AT EACH INDEX

        # # Recursive
        # from functools import cache
        # @cache
        # def dp(i: index):
        #     lis = 1  # initialize to 1
        #     for j in range(i):
        #         if nums[i] > nums[j]:  # == is not increasing
        #             lis = max(lis, dp(j) + 1)
        #     return lis
        # return max(dp(i) for i in range(len(nums)))

        # Iterative
        n = len(nums)
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        return max(lis)

