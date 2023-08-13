class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        def backtrack(curr, i):  # i is position in digit
            if i == len(digits):
                # answer.append(curr[:])  # we are not returning a list of characters but a string
                answer.append(''.join(curr[:]))
                return
            digit = digits[i]
            chars = mapping[digit]  # a, b, c
            for char in chars:
                curr.append(char)
                backtrack(curr, i + 1)
                curr.pop()
        if not digits:
            return []
        answer = []
        backtrack([], 0)
        return answer

