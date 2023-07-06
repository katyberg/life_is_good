# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            return node
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root
        # Note that other than the newly created node got returned to the leaf node,
        # every other node gets returned to be attached to the parent (as it already does)
        # ex: [4,2,7,1,3,null,null]
        #      5 is returned to be attached to left side of 7 (new connection)
        #      7 is returned to be attached to right side of 4 (as it originally does)
