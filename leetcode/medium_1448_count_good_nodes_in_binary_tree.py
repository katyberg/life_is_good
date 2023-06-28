# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Intuition: DFS, pre-order but left/right either can be first (does not matter)
        def dfs(root: TreeNode, max: int):
            if not root:
                return 0
            is_good = 0
            if root.val >= max:
                is_good = 1
                max = root.val
            return is_good + dfs(root.left, max) + dfs(root.right, max)
        # return dfs(root, 0)  # This is WRONG!!!! val has range [-10^4, 10^4]
        return dfs(root, float('-inf'))

