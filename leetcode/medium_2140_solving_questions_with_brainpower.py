class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Intuition:
        # Because there is "maximum points" and choice will affect result,
        # it is likely a DP problem.
        # There are three things we need to determine:
        # 1. DP Recurrence pattern
        #    => go through array, find max of starting index i
        #       for each index i as starting point, get the score
        # 2. Base cases
        # 3. Memoization
        #    => the state is dp score at index i

        # THIS IS A GOOD TRY BUT IS NOT CORRECT SOLUTION....!!!! X-(
        # def dp(i: int):
        #     if i == n - 1:
        #         return questions[i][1]  # [score, brainpower]
        #     j = i
        #     score = question[i][0]
        #     while j < n:
        #         j += question[j][1] + 1
        #         score += question[j][0]
        #     return score
        # n = len(questions)
        # return max([dp(i) for i in range(n)])

        from functools import cache
        @cache
        def dp(i: int):
            if i >= n:
                return 0
            # at each index, we can solve the problem or not
            # solve => score is added to the next dp
            # skip => score is not added to the next dp
            # dp represents the max score starting from next item
            # we take the max of the two
            cur_score = questions[i][0]
            next_i = i + questions[i][1] + 1  # notice the +1
            return max(cur_score + dp(next_i), dp(i + 1))
        n = len(questions)
        return dp(0)

# Compare this to https://leetcode.com/problems/longest-increasing-subsequence/

# # If not using @cache:
#     def mostPoints(self, questions: List[List[int]]) -> int:     
#         n = len(questions)
#         dp = [0] * n
#        
#         def dfs(i):
#             if i >= n:
#                 return 0
#             if dp[i]:
#                 return dp[i]
#             points, skip = questions[i]
#
#             # dp[i] = max(skip it, solve it)
#             dp[i] = max(dfs(i + 1), points + dfs(i + skip + 1))
#             return dp[i]
#        
#         return dfs(0)

