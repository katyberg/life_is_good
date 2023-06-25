class Solution:
    def removeDuplicates(self, s: str) -> str:
        def _x(s: str):
            stack = []
            for c in s:
                if stack and stack[-1] == c:
                    stack.pop()  # pop the stack (remove from end of list)
                else:
                    stack.append(c)  # push to stack (append to end of list)
            return ''.join(stack)  # stack is actually the list we want
        
        test = 'aaabbbacadd'
        result = _x(test)
        print(f'{test} will give result: {result}')
        # This will print: aaabbbacadd will give result: abaca
        # Previously I misunderstood the question therefore could not get the answer right!!!!
        # Now that I understnad the actual requirement the function is extremely simple!
        return _x(s)
