# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Intuition:
        # BFS, use deque
        # 1. Put each layer in an array
        # 2. flag reverse 0 -> 1 -> 0 -> 1 -> etc
        #    if reverse => reverse the array
        # 3. add layer to result array and return
        if not root:
            return []
        queue = deque([root])
        result = []
        reverse = False
        while queue:
            layer_len = len(queue)
            layer_node_vals = []
            for _ in range(layer_len):
                node = queue.popleft()
                # I can also check reverse here and use appendleft if reverse is True,
                # But I don't think it is much different reversing at the end....
                layer_node_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse:
                layer_node_vals = layer_node_vals[::-1]  # can also use reverse() in-place reverse
            reverse = not reverse
            result.append(layer_node_vals)
        return result

