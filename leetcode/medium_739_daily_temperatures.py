class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     n = len(temperatures)
    #     result = [0] * n
    #     stack = []
    #     for i in range(n):
    #         while stack:  # INFINITE LOOP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #             top = stack[-1]
    #             if temperatures[i] > temperatures[top]:  # stack[-1] is the top of the stack
    #                 j = stack.pop()
    #                 result[j] = i - j
    #         stack.append(i)
    #     return result

    # NOTE THAT MY SOLUTION ABOVE CREATES AN INFINITE LOOP!!!!!!!!!!!!!!!!
    # THE CONDITION SHOULD BE: while stack and temperatures[i] > temperatures[top]!
    # BECAUSE THE STACK WILL NOT BE EMPTY WITHIN THIS LOOP!
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        
        return answer
