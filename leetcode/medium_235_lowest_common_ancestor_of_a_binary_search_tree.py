# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # At one point, we will reach a node where p/q are on either side, that's the LCA.
        curr = root
        while curr:  # All Node.val are unique.
            if p.val < curr.val and q.val < curr.val:
                # self.lowestCommonAncestor(root.left, p, q)  # this causes infinite loop!!!!
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                # self.lowestCommonAncestor(root.right, p, q)  # this causes infinite loop!!!!
                curr = curr.right
            else:  
                # one smaller and the other bigger (don't care which one is which)
                # if we reach ANY node (first), that node is the LCA
                return curr

