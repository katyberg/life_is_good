class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Intuition:
        # Brute force - I drew the brute-force graph, but I graph was not good at coming to
        # a solution.... :-( In my graph, each tree is coin1*1, coin1*2, etc....
        # In the best solutions I found, the recurrence relation or the state is:
        # ====> THE MIN NUMBER OF COINS NEEDED TO ADD UP TO AN AMOUNT,
        #       AND THE AMOUNT ITSELF IS THE STATE!!!!
        #       WHO WOULD HAVE THOUGHT OF THAT!?!? :-(

        # This is a great video explaination of bottom-up approach:
        # https://youtu.be/H9bfqozjoqs
        # I like bottom up solution because it is more intuitive!
        # Example: [1, 3, 4, 5] amount=7
        # dp[0] = 0
        # dp[1] = 1  <= $1 x 1
        # dp[2] = 2  <= $1 x 2
        # dp[3] = 1  <= $3 x 1
        # dp[4] = 1  <= $4 x 1
        # dp[5] = 1  <= $5 x 1
        # dp[6] = 2  <= $3 x 2 or $1 x 1 + $5 x 1
        # dp[7] = 2  <= $3 x 1 + $4 x 1

        dp = [math.inf] * (amount + 1)  # from 0 to amount, initialize to inf because we want min
        # ^ this is memoization!
        # It represents the min number of coins needed to add up to each amount
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                # if we take this coin
                amount_left = i - coin
                if amount_left >= 0:
                    dp[i] = min(dp[i], 1 + dp[amount_left])
        # return dp[amount - 1] if dp[amount - 1] != math.inf else -1
        return dp[amount] if dp[amount] != math.inf else -1  # MISTAKE!!!!


        # Running through algorithm, this is basically brute force with momoization....
        # dp[1] coin=1 => amount_left = 0 => min(math.inf, 1 + dp[0]) = min(math.inf, 1) = 1
        # dp[1] coin=3 => amount_left = -2 x
        # dp[1] coin=4 => amount_left = -3 x
        # dp[1] coin=5 => amount_left = -4 x
        # ==> dp[1] = 1
        # dp[2] coin=1 => amount_left = 0 => min(math.inf, 1 + dp[1]) = min(math.inf, 1 + 1) = 2
        # dp[2] coin=3 => amount_left = -1 x
        # dp[2] coin=4 => amount_left = -2 x
        # dp[2] coin=5 => amount_left = -3 x
        # ==> dp[2] = 2
        # dp[3] coin=1 => amount_left = 2 => min(math.inf, 1 + dp[2]) = min(math.inf, 1 + 2) = 3
        # dp[3] coin=3 => amount_left = 0 => min(3, 1 + dp[0]) = min(3, 1 + 0) = 1
        # dp[3] coin=4 => amount_left = -2 x
        # dp[3] coin=5 => amount_left = -3 x
        # ==> dp[3] = 1
        # ....
