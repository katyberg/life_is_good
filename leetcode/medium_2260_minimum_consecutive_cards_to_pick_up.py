from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # # BELOW IMPLEMENTATION IS WRONG!!!!
        # # IT ASSUMES THAT FIRST NUMBER HAS TO FIND A MATCH!
        # # TEST [95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]
        # # FAILED!!!!
        # # sliding window
        # # constraint - have not found matching card with left
        # # constraint broken: found matching card -> increment left
        # # keep track of min # of cards to pick up
        # # O(N)
        # left = 0
        # min_num_card = float(inf)
        # for right in range(len(cards)):  # will not enter if cards has one item
        #     num = cards[right]
        #     while left != right and num == cards[left]:
        #         min_num_card = min(min_num_card, right - left + 1)
        #         print(f'num={num}, len={right - left + 1}')
        #         left += 1
        # if min_num_card == float(inf):
        #     return -1
        # return min_num_card

        # This problem is so easy to solve with hash table!!!!
        # And it has the best runtime!!!!
        # Also note that we don't need to store ALL indeces, just calculate min on the fly.
        index_hash = defaultdict(int)
        # To find min, initialize min to infinity
        # ans = float('inf')
        ans = math.inf
        for i, card in enumerate(cards):
            # If I already have this card in index_hash, calculate the min and reset index value.
            # Otherwise add it to index_hash
            if card in index_hash:
                ans = min(ans, i - index_hash[card] + 1)
            index_hash[card] = i
        return ans if ans < math.inf else -1

