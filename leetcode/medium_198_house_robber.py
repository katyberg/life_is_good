class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic programming - 3 things:
        # 1. Memoization
        # 2. Recursion - $ I get if I rob a particular hose (at index i)
        # 3. Base case:
        #    - rob house i=0
        #    - rob house i=1

        # Time complexity is O(N), Space complexity is also O(N)!!!!

        # Recursive approach (top-down)  <= this beats 98.76% of users
        # nums = [2,7,9,3,1]
        #                      dp(4)
        #                    /       \
        #                dp(2)       dp(3)
        #                /  \        /  \
        #            dp(0)  dp(1) dp(1)  dp(2)
        #
        def dp(i: int):  # i is the index of the houses            
            # base case
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            if i in mem:
                return mem[i]
            else:
                # max between ROB the house OR NOT ROB the house
                # IMPORTANT!!!! DO NOT FORGET TO ADD TO MEMORIZATION!
                # OTHERWISE WE WILL NOT HAVE MOMORIZATION!!!!
                # return max(nums[i] + dp(i - 2), dp(i - 1))
                m = max(nums[i] + dp(i - 2), dp(i - 1))
                mem[i] = m
                return m
        mem = {}
        max_money = dp(len(nums) - 1)  # 1 <= nums.length <= 100
        return max_money

        # # Recursive approach USING @cache  <= this beats 69.77% of users!!!!
        # # IT'S SLOWER THAN MY OWN MEMORIZATION DICTIONARY.... SURPRISING!!!!
        # from functools import cache
        # @cache
        # def dp(i: int):  # i is the index of the houses            
        #     # base case
        #     if i == 0:
        #         return nums[0]
        #     elif i == 1:
        #         return max(nums[0], nums[1])
        #     else:
        #         # max between ROB the house OR NOT ROB the house
        #         # IMPORTANT!!!! DO NOT FORGET TO ADD TO MEMORIZATION!
        #         # OTHERWISE WE WILL NOT HAVE MOMORIZATION!!!!
        #         # return max(nums[i] + dp(i - 2), dp(i - 1))
        #         return max(nums[i] + dp(i - 2), dp(i - 1))
        # max_money = dp(len(nums) - 1)  # 1 <= nums.length <= 100
        # return max_money

        # # Iterative approach (bottom-up)  <= this beats 54.30% of users
        # # 1 <= nums.length <= 100
        # if len(nums) == 1:  # not needed
        #     return nums[0]
        # elif len(nums) == 2:
        #     return max(nums[0], nums[1])
        # mem = [0] * len(nums)
        # mem[0] = nums[0]
        # mem[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     mem[i] = max(nums[i] + mem[i - 2], mem[i - 1])
        #     print(f'mem = {mem}')
        # return mem[len(nums) - 1]

        # # This iteration improves space requirement to O(1) because we only keeps 2 entries
        # # ^   <= this beats 40.06% of users
        # # To avoid out of bounds error from setting base case
        # if len(nums) == 1:
        #     return nums[0]
        # n = len(nums)
        # # Base cases
        # back_two = nums[0]
        # back_one = max(nums[0], nums[1])
        # for i in range(2, n):
        #     # back_two becomes back_one, and back_one gets updated
        #     back_one, back_two = max(back_one, back_two + nums[i]), back_one
        # return back_one

