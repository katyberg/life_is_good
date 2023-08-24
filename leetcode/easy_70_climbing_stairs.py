class Solution:
    from functools import cache
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i: int):
            if i > n:
                return 0
            elif i == n:
                return 1
            return dp(i + 1) + dp(i + 2)
        return dp(0)


# n = 3 => base case i=2 or i=1
#          dp(0)
#        /       \
#    dp(1)       dp(2)
#    /    \      /    \
#  dp(2) dp(3) dp(3) dp(4)
