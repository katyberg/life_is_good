# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Intuition:
        # This is DFS, pre-order traversal.
        # In addition, we need to identify "leaf node"
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:  # if we are at LEAF node, check if targetSum is 0.
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

