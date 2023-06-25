from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Criteria:
        # - digits not the same (num1 != num2)
        # - digit sums are the same (calculate digit sum)

        # Build a dictionary with digit sum as key, set of nums encountered as value
        # Go through all the values, and find the max sum of two numbers for all keys
        # => sort set from most significant to least significant digit, return the top 2

        # def sum_of_digits(num):
        #     digit_sum = 0
        #     while num:
        #         digit_sum += num % 10  # % 10 to get last digit (least significant)
        #         num //= 10  # floor division 10 to get all number except the last digit
        #     return digit_sum
        def _digit_sum(num:int):
            return sum([int(d) for d in str(num)])
        # NOTE THAT I CANNOT USE A SET HERE, I HAVE TO USE A LIST!!!!
        # nums =[4,6,10,6] SET  => digit_sum_hash={4: {4}, 6: {6}, 1: {10}}   max_sum=-1
        #                  LIST => digit_sum_hash={4: {4}, 6: {6,6}, 1: {10}} max_sum=12
        # !!!!
        # digit_sum_hash = defaultdict(set)
        digit_sum_hash = defaultdict(list)
        max_sum = -1
        for num in nums:
            digit_sum = _digit_sum(num)                
            digit_sum_hash[digit_sum].append(num)
        print(digit_sum_hash)
        for k, v in digit_sum_hash.items():
            if len(v) >= 2:  # question asks for any 2 numbers, single num does not count!
                s = sorted(v, reverse=True)
                print(s)
                max_sum = max(max_sum, s[0] + s[1])
                print(max_sum)
        return max_sum


