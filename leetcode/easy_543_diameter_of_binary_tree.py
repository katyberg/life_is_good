# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = float('-inf')
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Intuition:
        # dfs, post-order
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            # recur left and right
            left = dfs(root.left)  # left represents longest number of edges on left
            right = dfs(root.right)  # left represents longest number of edges on right
            # calculate current depth
            
            # BELOW IS WRONG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # BELOW CALCULATES CURRENT TOTAL NUMBER OF NODES INCLUDING CURRENT ROOT....
            # cur_diameter = 1 + left + right
            
            # Instead, we want to return the longer path comparing left and right
            # but keep track of the current max depth (which is left+right+1) as we go
            # Think about following case:
            #            1
            #           / \
            #          2   8
            #         / \
            #        3   4
            #             \
            #              5
            #               \
            #                6
            #                 \
            #                  7
            longer_path = max(left, right) + 1
            cur_diameter = left + right
            # update max depth up to this point (this root)
            self.max_diameter = max(self.max_diameter, cur_diameter)
            print(f'At node {root.val}: left={left}, right={right}, longer_path={longer_path}, cur_diameter={cur_diameter}, self.max_diameter={self.max_diameter}')
            return longer_path
        if not root:
            return 0  # I need this because dfs does not update self.max_diameter when root is None
        dfs(root)
        return self.max_diameter

