# This problem is a BFS/DFS but also a backtracking (pretty similar ideas)....
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # Intuition:
        # Graph the tree, start with 0 < d <= 9
        # need a separate function to generate the next number +k < 10 and -k >= 0
        # when depth is n add to answer
        def get_next_valid_digits(digit: int): 
            if k == 0:
                return [digit]
            next_valid_digits = []
            if digit + k < 10:
                next_valid_digits.append(digit + k)
            if digit - k >= 0:
                next_valid_digits.append(digit - k)
            return next_valid_digits
                        
        def backtrack(curr: list, digit: int):
            if len(curr) == n:
                # answer.append(int(''.join(list(map(str, curr)))))  # this works too.
                answer.append(int(''.join([str(d) for d in curr])))
                return
            next_valid_digits = get_next_valid_digits(digit)
            for d in next_valid_digits:
                curr += str(d)
                backtrack(curr, d)
                curr.pop()
        
        answer = []
        for i in range(1, 10):  # first number has domain space 1 - 9
            backtrack([i], i)
        return answer

# # Ok! This is much simplier.... Duh! X(
# class Solution:
#     def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
#         result = []
#         def backtrack(i, prefix):
#             if i == n:
#                 result.append(prefix)
#                 return
#             last_digit = prefix % 10
#             if 0 <= last_digit + k <= 9:
#                 backtrack(i + 1, prefix * 10 + last_digit + k)
#             if k > 0 and 0 <= last_digit - k <= 9:
#                 backtrack(i + 1, prefix * 10 + last_digit - k)
#         for i in range(1, 10):
#             backtrack(1, i)
#         return result
    

# # Ps: I originally have the following for which is ALL WRONG! Check question carefully!!!!
#             # if k is 0, only one option is possible: digit itself. Otherwise infinite loop!
#         def get_next_valid_digits(digit: int): 
#             next_valid_digits = []
#             if k == 0:
#                 return [digit]
#             next_digit = digit + k
#             while next_digit < 10:
#                 next_valid_digits.append(next_digit)
#                 next_digit += k
#             next_digit = digit - k    
#             while next_digit >= 0:
#                 next_valid_digits.append(next_digit)
#                 next_digit -= k
#             return next_valid_digits

