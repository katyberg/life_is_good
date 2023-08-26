class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # I first saw this problem at mock interview example:
        # https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/713/interviews-and-tools/4548/
        # The O(N) solution is not easy to come by, but the most important trick is:
        # when the modulo of prefix sum at a certain index i repeats with previous index j,
        # it means the sum of the subarray between i and j are multiple of k.
        # Example: [23, 2, 4, 6, 7]
        # Prefix sum: [23, 25, 29, 35, 42]
        # Prefix sum modulo: [5, 1, 5, 5, 0]
        
        # # Brute Force
        # # Time complexity: O(N^2)
        # # Space complexity: O(1)
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         curr += nums[j]
        #         if curr % k == 0:
        #             return True
        # return False
        # Ps: potential improvement is to use momoization (hash) to reduce duplicated calculation
        #     of the array sum.

        # Better Approach
        # Time Complexity: O(N)
        # Space Complexity: O(N) <-- trade off time with space
        # IMPORTANT!!!! WE HAVE TO INITIALIZE dic = {0: -1} OTHERWISE BELOW USE CASE DOES NOT WORK!
        # USE CASE: nums=[23,2,4,6,6] k=7 prefix_sum=[23,25,29,35,41] modulo=[2,4,1,0,6]
        curr = 0
        # dic = {}  # key is the modulo and value is the index
        dic = {0: -1}
        for i in range(len(nums)):
            curr += nums[i]
            curr_mod = curr % k
            if curr_mod in dic:
                if i - dic[curr_mod] > 1:
                    return True
            else:
                dic[curr_mod] = i  # just need to store one of them
        return False

