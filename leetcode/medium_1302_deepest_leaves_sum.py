# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # Intuition:
        # Use BFS, at last layer, add all the nodes
        # "last layer" - all nodes have no children
        if not root:  # not needed because N=>[1, 104] but have it anyway
            return 0
        queue = deque([root])
        result = 0  # all nodes are positive 1 <= Node.val <= 100, N=>[1, 104] min = 1
        while queue:
            layer_len = len(queue)
            # keep track of the number of nodes that have no children
            layer_num_leaf = 0
            layer_sum = 0
            for _ in range(layer_len):
                node = queue.popleft()
                layer_sum += node.val
                if not node.left and not node.right:  # encounters a leaf node
                    layer_num_leaf += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if layer_num_leaf == layer_len:  # last layer all nodes are leaf nodes
                result = layer_sum
        return result
    
    # # Another interesting solution other's have:
    # def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    #     nodes = [root]
    #     while len(nodes) > 0:
    #         children = []
    #         for n in nodes:
    #             if n.left:
    #                 children.append(n.left)
    #             if n.right:
    #                 children.append(n.right)
    #         if len(children) == 0:
    #             break
    #         else:
    #             nodes = children
    #     return sum([n.val for n in nodes])

