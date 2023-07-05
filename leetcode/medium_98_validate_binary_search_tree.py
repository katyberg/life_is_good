# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # This implementation was suggested by lecture, it is faster!
        # Each node needs to satisfy [lower_bound, upper_bound]
        # Important property is upper_bound for left will always be root node value, 
        # lower_bound for right subtree will always be root node value
        def dfs(root: Optional[TreeNode], lower_bound, upper_bound):
            if not root:
                return True
            if not (lower_bound < root.val < upper_bound):
                return False
            left = dfs(root.left, lower_bound, root.val)
            right = dfs(root.right, root.val, upper_bound)
            return left and right
        return dfs(root, float('-inf'), float('inf'))

        # # Below implementation works but is not very fast....
        # is_valid = True
        # def dfs(root: Optional[TreeNode]):
        #     # THIS IS IMPORTANT! WITHOUT THIS, is_valid WILL NOT BE UPDATED INSIDE DFS!!!!
        #     nonlocal is_valid
        #     if not root:
        #         return (float('inf'), float('-inf'))
        #     (left_min, left_max) = dfs(root.left)
        #     (right_min, right_max) = dfs(root.right)
        #     if not (left_max < root.val < right_min):
        #         is_valid = False
        #     return (min(left_min, right_min, root.val), max(left_max, right_max, root.val))
        # dfs(root)
        # return is_valid

        # BELOW IMPLEMENTATION IS WRONG!!!!ITUITION IS WRONG AS WELL!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Ex: [5,4,6,null,null,3,7]
        # 3 violates the BST on the right side, so we have to traverse the whole tree!
        #
        # # Intuition:
        # # DFS, pre-order
        # # Originally I started with post-order. At each node,
        # # validate left subtree is valid, right subtree is valid, AND left < node.val < right.
        # # If I check left subtree is valid, left < node.val < right, then right subtree is valid
        # # I could potentially skip the whole right tree if not necessary, if left is invalid.
        # # So I thought I change my mind to in-order.
        # # BUT even better is to do pre-order => I potentially can skip the BOTH left/right trees!
        # # Need to ask if it's True for empty tree, but in this question N >= 1.
        # # For my base case, empty node is True.
        # if not root:
        #     return True
        # # is left < node.val < right
        # left = right = True  # need this for single node use case
        # if root.left:
        #     left = root.val > root.left.val
        # if root.right:
        #     right = root.val < root.right.val
        # node_valid = left and right
        # return node_valid and self.isValidBST(root.left) and self.isValidBST(root.right)

