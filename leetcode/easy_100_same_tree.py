# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # # Intuition:
        # # If two trees have the same in-order traversal they have the same structure!?!?
        # # THIS IS WRONG!!!!!!!!!!!!!!!!
        # # EXAMPLE: p=[1,1] q=[1,null,1] BOTH HAVE IN-ORDER TRAVERSAL RESULT [1,1]!!!!
        # def dfs(root: TreeNode):
        #     if not root:
        #         return []
        #     return dfs(root.left) + [root.val] + dfs(root.right)
        # return dfs(p) == dfs(q)

        # I will still use DFS, in-order traversal.
        # Instead of constructing a result list, I traverse them together, just compare as I go.
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

