# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_depth = math.inf  # initialize to POSITIVE infinity
        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Intuition:
        # - need to traverse the entire tree to find min or max depth
        # - this is dfs, in-order traversal (left->root->right)
        #   do something part is to add the current node to depth until leaf node is reached.
        # - traverse down the tree, when hit "leaf" node, calculate the length (keep track of min)
        def _dfs(root, depth):
            if not root:
                return
            # leaf node is reached, calculate min_depth
            if not root.left and not root.right:
                print(f'self.min_depth={self.min_depth}, depth={depth}')
                self.min_depth = min(self.min_depth, depth)
            # if I am not at leaf node, add 1 to the depth and recur
            else:
                _dfs(root.left, 1 + depth)
                _dfs(root.right, 1 + depth)
        if not root:
            return 0
        else:
            _dfs(root, 1)
        return self.min_depth

        # # Iteratively using a queue
        # if not root:
        #     return 0
        # q = [(root,1)]
        # while q:
        #     node,depth = q.pop(0)
        #     if not node.left and not node.right:
        #         return depth
        #     if node.left:
        #         q.append((node.left,depth+1))
        #     if node.right:
        #         q.append((node.right,depth+1))

