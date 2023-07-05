# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Intuition:
        # Brute force - traverse the tree -> list, compare all two elements find min => O(N^2)!
        # Brute force (better) - traverse the tree -> list, sort list, go through list and
        # find min diff of two adjecent elements => O(NlogN) because of the sort.
        # Because it is BT, in-order traversal generates sorted list => O(N)

        # 82 ms, but run again 68 ms?!
        def dfs_inorder(root: Optional[TreeNode]):
            # return the in-order traversal list
            if not root:
                return []
            return dfs_inorder(root.left) + [root.val] + dfs_inorder(root.right)
        inorder = dfs_inorder(root)
        # we have at least 2 nodes N => [2, 104]
        # min_diff = 0  # STUPID MISTAKE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        min_diff = math.inf  # or float('inf')
        for i in range(len(inorder) - 1):
            min_diff = min(min_diff, abs(inorder[i] - inorder[i+1]))
        return min_diff

        # 76 ms (maybe tiny bit faster without list addition, but doesn't matter....)
        # inorder = []
        # def dfs_inorder(root: Optional[TreeNode]):
        #     # return the in-order traversal list
        #     if not root:
        #         return
        #     dfs_inorder(root.left)
        #     inorder.append(root.val)
        #     dfs_inorder(root.right)
        # dfs_inorder(root)
        # min_diff = math.inf
        # for i in range(len(inorder) - 1):
        #     min_diff = min(min_diff, abs(inorder[i] - inorder[i+1]))
        # return min_diff

