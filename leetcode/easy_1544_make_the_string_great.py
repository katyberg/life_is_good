class Solution:
    def makeGood(self, s: str) -> str:
        matching = {}
        for l in 'abcdefghijklmnopqrstuvwxyz':
            matching[l] = l.upper()
            matching[l.upper()] = l
        print(matching)
        stack = []
        for c in s:
            if stack and stack[-1] == matching[c]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

