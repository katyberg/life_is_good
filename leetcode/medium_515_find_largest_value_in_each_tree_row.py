# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            cur_level_len = len(queue)
            cur_level_max = float('-inf')
            for _ in range(cur_level_len):
                node = queue.popleft()
                cur_level_max = max(cur_level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(cur_level_max)
        return ans

