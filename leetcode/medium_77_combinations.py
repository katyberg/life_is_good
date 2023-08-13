class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, i):
            if len(curr) == k:
                answer.append(curr[:])
                return
            for num in range(i, n + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop() 
        answer = []
        backtrack([], 1)
        return answer


# BELOW SOLUTION IS WRONG!!!! FOR n=4, k=2
# IT OUTPUT [[1,2],[1,3],[1,4],[2,2],[2,3],[2,4],[3,2],[3,3],[3,4],[4,2],[4,3],[4,4]]
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         # i keeps track of the position to start for each branch, j keeps track of depth
#         def backtrack(curr, i, j):
#             print(f'curr={curr}, i={i}, j={j}')
#             if j == k:
#                 answer.append(curr[:])
#                 return
#             for num in range(i, n + 1):  # num will be from 1 to n in the beginning
#                 curr.append(num)
#                 backtrack(curr, i + 1, j + 1)
#                 curr.pop()
#         answer = []
#         backtrack([], 1, 0)
#         return answer
# # OUTPUT:
# curr=[], i=1, j=0
# curr=[1], i=2, j=1
# curr=[1, 2], i=3, j=2
# curr=[1, 3], i=3, j=2
# curr=[1, 4], i=3, j=2
# curr=[2], i=2, j=1
# curr=[2, 2], i=3, j=2
# curr=[2, 3], i=3, j=2
# curr=[2, 4], i=3, j=2
# curr=[3], i=2, j=1
# curr=[3, 2], i=3, j=2
# curr=[3, 3], i=3, j=2
# curr=[3, 4], i=3, j=2
# curr=[4], i=2, j=1
# curr=[4, 2], i=3, j=2
# curr=[4, 3], i=3, j=2
# curr=[4, 4], i=3, j=2

