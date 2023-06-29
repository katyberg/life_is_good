# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Intuition:
        # DFS, pre-order
        # THIS PROBLEM IS SOMEHOW PRETTY HARD FOR ME....
        # I STRUGGLE WITH WHAT SHOULD BE PASSED INTO THE RECURSIVE CALL AND WHAT SHOULD BE RETURNED!!!!
        # IN THE END, THE KEY IS FOLLOWING!!!!
        # The least common ancestor would be the node:
        # 1. both the subtree recursions return a True flag.
        # 2. itself is one of p or q and one of the subtree recursions returns a True flag.
        # def lca(node):
        #     if not node:
        #         return False
        #     left = lca(node.left)
        #     right = lca(node.right)
        #     node_is_p_or_q = (node == p) or (node == q)
        #     # check 1 and 2 conditions above -> either satisfies means current node is the answer
        #     if (left and right) or (node_is_p_or_q and (left or right)):
        #         self.ans = node
        #     # otherwise, continue to pass on the information to the parent
        #     return node_is_p_or_q or left or right
        # lca(root)
        # return self.ans

        # Another solution from Tushar:
        # https://youtu.be/13m9ZCB8gjw
        def lca(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = lca(node.left)
            right = lca(node.right)
            if left and right:
                return node
            elif left or right:
                return left if left else right
            else:
                return None
        return lca(root)


