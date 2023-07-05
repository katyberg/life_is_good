# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0  # min is 0 because 1 <= Node.val <= 105
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Intuition:
        # Brute force: DFS check all nodes O(N) but not utilizing BST property
        # DFS, pre-order
        # At each node, add to sum if within range, selectively go left/right based on range
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            node_val = root.val
            # ps: low, high comes from parent function....
            # maybe it's best practice to declare nonlocal even though we do not modify them.
            nonlocal low, high
            # if node_val >= low and node_val <= high:
            if low <= node_val <= high:  # we can directly chain operators
                self.sum += node_val
            # all nodes are unique, so branch will not have same value
            if node_val > low:
                dfs(root.left)
            if node_val < high:
                dfs(root.right)
        dfs(root)
        return self.sum

    # # This particular problem does not require an internal function and an outside sum,
    # # but it's fine :-)
    # # Here is an alternative approach
    # if root == None:
    #         return 0
    #     res = 0
    #     if low <= root.val <= high:
    #         res += root.val
    #     if root.val <= high:
    #         res += self.rangeSumBST(root.right, low, high)
    #     if root.val >= low:
    #         res += self.rangeSumBST(root.left, low, high)

    #     return res

