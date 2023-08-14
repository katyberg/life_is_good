class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def get_next_valid_digits(digit: int):
            next_valid_digits = []
            for i in range(digit + 1, 10):  # digit +1 up to 9
                if i <= n:  # no point to add any digit that is greater than n itself.
                    next_valid_digits.append(i)
            return next_valid_digits

        def backtrack(curr: list, digit: int, curr_sum: int):
            # Base cases
            if curr_sum > n:  # Improvement: ex: k=3,n=7 => we skip 8 and 9
                return  # check digit > n also works the same way
            if (curr_sum == n and len(curr) < k):  
                return
            if len(curr) == k:
                if curr_sum == n:
                    answer.append(curr[:])  # IMPORTANT!!!! REMEMBER TO MAKE A COPY!!!!
                return
            # Recur
            next_valid_digits = get_next_valid_digits(digit)
            for digit in next_valid_digits:
                curr.append(digit)
                curr_sum += digit
                backtrack(curr, digit, curr_sum)
                curr.pop()
                curr_sum -= digit

        answer = []
        for i in range(1, 10):  # start with 1 to 9
            curr = [i]
            backtrack(curr, i, i)
            curr.pop()
        return answer

