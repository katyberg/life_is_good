class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])  # make a copy
                # IMPORTANT!!!!
                # nums[:] = foo invokes slice assignment on the object that nums refers to,
                # thus making a copy of the contents of the original array.
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()  # note we have to pop off after each backtrack call
        ans = []
        backtrack([])
        return ans
