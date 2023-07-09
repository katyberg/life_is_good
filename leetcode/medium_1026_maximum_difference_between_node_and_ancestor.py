# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import namedtuple
MaxMin = namedtuple('MaxMin', 'max_val min_val')
class Solution:
    def __init__(self):
        self.max_diff = float('-inf')

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # # BELOW ANSWER WAS WRONG FOR THIS TEST CASE: [2,4,3,1,null,0,5,null,6,null,null,null,7]
        # # I OUTPUTTED 7 BUT CORRECT ANSWER IS 5....
        # # I DON'T UNDERSTAND WHY I GET 7!?!
        # # path=[2, 4]
        # # path=[2, 4, 1]
        # # path=[2, 4, 1, 6]
        # # path=[2, 3]
        # # path=[2, 3, 0]
        # # path=[2, 3, 0, 5]
        # # path=[2, 3, 0, 5, 7]
        # # Intuition:
        # # Find all paths to leaf node, for each path sort the nodes and calculate max diff
        # def dfs(root, path, max_diff):
        #     if not root:
        #         return max_diff
        #     path.append(root.val)
        #     print(f'path={path}')
        #     # If at leaf node, calculate max of path
        #     if not root.left and not root.right:
        #         path_max_diff = max(path) - min(path)
        #         max_diff = max(path_max_diff, max_diff)
        #         return max_diff
        #     else:
        #         return max(dfs(root.left, path, max_diff), dfs(root.right, path, max_diff))
        # max_diff = float('-inf')
        # return max(dfs(root.left, [root.val], max_diff), dfs(root.right, [root.val], max_diff))
        
        # # More correct way after watching Youtube video:
        # # https://youtu.be/8pp0sszQBx4
        # # Intuition: dfs, post-order
        # def dfs(root: Optional[TreeNode]) -> MaxMin:  # [max, min] along left or right paths
        #     if not root:
        #         return MaxMin(max_val=float('-inf'), min_val=float('inf'))
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     # calculate max diff between left and right (including root value in consideration)
        #     # left_max - left_min
        #     left_diff =  abs(max(root.val, left.max_val) - min(root.val, left.min_val))
        #     #  right_max - right_min
        #     right_diff = abs(max(root.val, right.max_val) - min(root.val, right.min_val))
        #     self.max_diff = max(self.max_diff, left_diff, right_diff)
        #     # calculate return value
        #     # NOTE: WHEN RETURNING WE NEED TO RETURN MAX/MIN OF THE WHOLE SUBTREE!!!! THNINK ABOUT IT!
        #     # [max_sub_tree, min_sub_tree]
        #     ret_val = MaxMin(max_val=max(root.val, left.max_val, right.max_val),
        #                      min_val=min(root.val, left.min_val, right.min_val))
        #     return ret_val
        # dfs(root)  # don't care about root return value
        # return self.max_diff

        # Implementation provided by Leetcode solution
        if not root:
            return 0
        # record the required maximum difference
        self.result = 0
        def helper(node, cur_max, cur_min):
            if not node:
                return
            # update `result`
            self.result = max(self.result, abs(cur_max-node.val),
                              abs(cur_min-node.val))
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)
        helper(root, root.val, root.val)
        return self.result

