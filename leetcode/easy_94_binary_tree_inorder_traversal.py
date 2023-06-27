# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursively
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # # Iteratively - THIS ONE IS HARD FOR ME :-( NEED TO MEMORIZE SOME....!!!!
        # result = []
        # stack = []
        # curr = root
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     result.append(curr.val)
        #     curr = curr.right
        # return result

