class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            '[': ']',
            '{': '}',
            '(': ')',
        }
        stack = []
        for c in s:
            if c in bracket:
                stack.append(c)  # push on stack
            else:
                if not stack:  # This is important**** ex: []} or just }
                    return False
                if c != bracket[stack.pop()]:
                    return False
        # Below are not needed because of **** above
        # if i >= len(s):  # ex: ]
        #     return False

        # if stack:  # if not empty we have unmatched bracket ex: {[[[[]]]]
        #     return False
        return not stack  # ex: []{

