class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):  # i is the index to start in each backtrack call
            if i > len(nums):
                return
            for j in range(i, len(nums)):
                curr.append(nums[j])
                answer.append(curr[:])
                backtrack(curr, j + 1)
                curr.pop()
        answer = [[]]
        backtrack([], 0)
        return answer


# # WRONG!!!!
# # Output: [[],[1],[1,2],[1,2,3],[1,3],[1,3,2],[2],[2,3],[3],[3,2]]
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(num, curr):
#             if len(curr) == len(nums):
#                 return
#             i = nums.index(num)
#             for n in nums[-i:]:
#                 print(f'num={num}, curr={curr}, i={i}, n={n}, nums[-i:]={nums[-i:]}')
#                 if n not in curr:
#                     curr.append(n)
#                     answer.append(curr[:])  # Remember to copy
#                     backtrack(n, curr)
#                     curr.pop()
#         answer = [[]]
#         backtrack(nums[0], [])  # 1 <= nums.length <= 10
#         return answer


# # THIS SOLUTION WORKS, BUT EXCEEDED TIME LIMIT!!!! FOR TEST CASE nums = [1,2,3,4,5,6,7,8,10,0]
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         # Intuition:
#         # This problem is very similar to the permutation problem
#         # https://leetcode.com/problems/permutations/description/
#         # except that each (valid) node in the tree is a solution itself and
#         # the solution is a set.
#         def backtrack(curr):
#             # print(f'++++ entering backtrack curr={curr}')
#             if len(curr) == len(nums):
#                 return
#             for num in nums:
#                 if num not in curr:
#                     curr.add(num)
#                     # print(f'num={num}, curr={curr}')
#                     if curr not in ans:
#                         # print(f'adding curr to ans')
#                         # OMG!!!! IMPORTANT!!!!
#                         # WE HAVE TO MAKE A COPY OF THE SET BEFORE ADDING TO ANS!!!!
#                         # ans.append(curr)
#                         ans.append(curr.copy())
#                     # print(f'ans={ans}')
#                     backtrack(curr)
#                     curr.remove(num)
#         ans = [set()]
#         backtrack(set())
#         answer = [list(s) for s in ans]
#         return answer

# # # IF WE DO NOT USE SET.COPY() THIS IS THE RESULT WE WILL SEE:
# # NOTICE THE OUTPUT BECOMES [[],[]]
# # ++++ entering backtrack curr=set()
# # num=1, curr={1}
# # adding curr to ans
# # ans=[set(), {1}]
# # ++++ entering backtrack curr={1}
# # num=2, curr={1, 2}
# # ans=[set(), {1, 2}]
# # ++++ entering backtrack curr={1, 2}
# # num=3, curr={1, 2, 3}
# # ans=[set(), {1, 2, 3}]
# # ++++ entering backtrack curr={1, 2, 3}
# # num=3, curr={1, 3}
# # ans=[set(), {1, 3}]
# # ++++ entering backtrack curr={1, 3}
# # num=2, curr={1, 2, 3}
# # ans=[set(), {1, 2, 3}]
# # ++++ entering backtrack curr={1, 2, 3}
# # num=2, curr={2}
# # ans=[set(), {2}]
# # ++++ entering backtrack curr={2}
# # num=1, curr={1, 2}
# # ans=[set(), {1, 2}]
# # ++++ entering backtrack curr={1, 2}
# # num=3, curr={3, 1, 2}
# # ans=[set(), {3, 1, 2}]
# # ++++ entering backtrack curr={3, 1, 2}
# # num=3, curr={3, 2}
# # ans=[set(), {3, 2}]
# # ++++ entering backtrack curr={3, 2}
# # num=1, curr={1, 2, 3}
# # ans=[set(), {1, 2, 3}]
# # ++++ entering backtrack curr={1, 2, 3}
# # num=3, curr={3}
# # ans=[set(), {3}]
# # ++++ entering backtrack curr={3}
# # num=1, curr={1, 3}
# # ans=[set(), {1, 3}]
# # ++++ entering backtrack curr={1, 3}
# # num=2, curr={1, 3, 2}
# # ans=[set(), {1, 3, 2}]
# # ++++ entering backtrack curr={1, 3, 2}
# # num=2, curr={3, 2}
# # ans=[set(), {3, 2}]
# # ++++ entering backtrack curr={3, 2}
# # num=1, curr={1, 3, 2}
# # ans=[set(), {1, 3, 2}]
# # ++++ entering backtrack curr={1, 3, 2}

# # # WHEN WE DO IT CORRECTLY (MAKING A COPY OF THE SET BEFORE APPENDING), WE GET FOLLOWING
# # ++++ entering backtrack curr=set()
# # num=1, curr={1}
# # adding curr to ans
# # ans=[set(), {1}]
# # ++++ entering backtrack curr={1}
# # num=2, curr={1, 2}
# # adding curr to ans
# # ans=[set(), {1}, {1, 2}]
# # ++++ entering backtrack curr={1, 2}
# # num=3, curr={1, 2, 3}
# # adding curr to ans
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}]
# # ++++ entering backtrack curr={1, 2, 3}
# # num=3, curr={1, 3}
# # adding curr to ans
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}]
# # ++++ entering backtrack curr={1, 3}
# # num=2, curr={1, 2, 3}
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}]
# # ++++ entering backtrack curr={1, 2, 3}
# # num=2, curr={2}
# # adding curr to ans
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}]
# # ++++ entering backtrack curr={2}
# # num=1, curr={1, 2}
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}]
# # ++++ entering backtrack curr={1, 2}
# # num=3, curr={3, 1, 2}
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}]
# # ++++ entering backtrack curr={3, 1, 2}
# # num=3, curr={3, 2}
# # adding curr to ans
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}]
# # ++++ entering backtrack curr={3, 2}
# # num=1, curr={1, 2, 3}
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}]
# # ++++ entering backtrack curr={1, 2, 3}
# # num=3, curr={3}
# # adding curr to ans
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}, {3}]
# # ++++ entering backtrack curr={3}
# # num=1, curr={1, 3}
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}, {3}]
# # ++++ entering backtrack curr={1, 3}
# # num=2, curr={1, 3, 2}
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}, {3}]
# # ++++ entering backtrack curr={1, 3, 2}
# # num=2, curr={3, 2}
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}, {3}]
# # ++++ entering backtrack curr={3, 2}
# # num=1, curr={1, 3, 2}
# # ans=[set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}, {3}]
# # ++++ entering backtrack curr={1, 3, 2}

