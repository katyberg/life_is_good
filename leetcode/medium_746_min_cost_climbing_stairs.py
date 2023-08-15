class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Ituition:
        # God please protect my father!!!!
        # Dynamic programming! 3 things:
        # state memoization => identify STATE: cost it takes to get to a stair
        # function => dp is cost to get to dp(i) is either dp(i-1) or dp(i-2)
        # base case => dp(0) and dp(1) cost=[10,15,20]
        #              dp(3) <- c=min(15,30)=15
        #   0+15=15 -> /  \ <- 10+20=30
        #   c=0 -> dp(1)  dp(2) <- c=min(10,15)=10
        #         0+10 -> /  \ <- 0+15
        #             dp(0)   dp(1)
        #             c=0      c=0

        # Using recursive approach
        def dp(i: int):  # i represents the ith stair
            # base case
            if i < 2:
                return 0
            if i in memoization:
                return memoization[i]
            else:
                # 2 <= cost.length <= 1000
                c = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
                memoization[i] = c
                return c
        
        memoization = {0: 0, 1: 0}
        min_cost = dp(len(cost))
        return min_cost

        # # Using iterative approach
        # n = len(cost) + 1
        # memoization = [0] * n
        # for i in range(2, len(cost) + 1):
        #     c = min(memoization[i - 1] + cost[i - 1], memoization[i - 2] + cost[i - 2])
        #     memoization[i] = c
        # return memoization[len(cost)]

