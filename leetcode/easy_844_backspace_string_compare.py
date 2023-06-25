class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def _typed(s: str):
            stack = []
            for c in s:
                if c is not '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return _typed(s) == _typed(t)

