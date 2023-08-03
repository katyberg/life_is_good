class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # # Intuition:
        # # We memorized "leftmost insert" and "rightmost insert",
        # # but this problem is different:
        # # 1. there is no repeating
        # # 2. if target exists return its index
        # # So we can modify the rightmost algo to include equal
        # l = 0
        # r = len(nums)
        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] == target:  # only add this line so if found just return the m
        #         return m
        #     elif nums[m] > target:  # the rest is equal to rightmost insert
        #         r = m
        #     else:
        #         l = m + 1
        # return l

        # BUT ACTUALLY I THOUGHT ABOUT THIS PROBLEM A LITTLE TOO MUCH!
        # JUST USE THE SEARCH, WHEN LOOP EXITS JUST RETURN LEFT!
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:  # go left
                r = m - 1
            else:
                l = m + 1
        return l
        
#         # REVIEW leftmost and rightmost insert:
#         # Leftmost insert:
#         l = 0
#         r = len(nums)
#         while l < r:
#             m = (l + r) // 2
#             if nums[m] >= target:
#                 r = m
#             else:
#                 l = m + 1
#         return l
#
#         # Rightmost insert:
#         l = 0
#         r = len(nums)
#         while l < r:
#             m = (l + r) // 2
#             if nums[m] > target:
#                 r = m
#             else:
#                 l = m + 1
#         return l
        
        
