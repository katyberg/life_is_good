# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:  # need to take care of None root because we access [-1] first later
            return []
        queue = deque([root])
        ans = []
        while queue:
            print(f'queue={queue}')
            ans.append(queue[-1].val)  # this is here because it's done once per level
            # remember to append the actual value of the node not the node itself!
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                # elif node.right:  # NOT elif!!!!!!!!!!!!!!!!
                if node.right:
                    queue.append(node.right)
        return ans

