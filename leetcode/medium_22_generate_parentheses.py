from collections import defaultdict
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Inutition - backtracking
        # Rule:
        # Tree starts with '('
        # Keep track of available parenthesis
        # end/base case -> available becomes empty
        def get_next_available(available: dict):
            next_available = []
            if available['('] > 0:
                next_available.append('(')
            if available[')'] > 0:
                next_available.append(')')
            return next_available
        
        def is_valid(curr: str):
            unmatched = 0
            for char in curr:
                if char == '(':
                    unmatched += 1
                elif char == ')':
                    unmatched -= 1
                # IMPORTANT!!!!
                # NOTICE THAT WILL ALWAYS BE 0 AT THE END, ONLY <0 IS INVALID CASE!!!!
                if unmatched < 0:  
                    return False
            return True

        def backtrack(curr: str, available: dict):
            if not available['('] and not available[')']:
                if is_valid(curr):
                    answer.append(curr)
                return
            next_available = get_next_available(available)
            for char in next_available:
                curr += char
                available[char] -= 1
                backtrack(curr, available)
                curr = curr[:-1]
                available[char] += 1
            
        available = {
            '(': n - 1,  # one '(' is used at the beginning, 1 <= n <= 8
            ')': n
        }
        answer = []
        backtrack('(', available)
        return answer

# # I like this solution provided as well!
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         answer = []
#         def backtracking(cur_string, left_count, right_count):
#             if len(cur_string) == 2 * n:
#                 answer.append("".join(cur_string))
#                 return
#             if left_count < n:
#                 cur_string.append("(")
#                 backtracking(cur_string, left_count + 1, right_count)
#                 cur_string.pop()
#             if right_count < left_count:
#                 cur_string.append(")")
#                 backtracking(cur_string, left_count, right_count + 1)
#                 cur_string.pop()
#         backtracking([], 0, 0)
#         return answer

