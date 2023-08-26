# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Intuition
        # Originally I thought of in-order traverl because the first example produces exact
        # solution. But it does not work for second example.
        # So it turns out which order of traversal does not matter. We just need to traverse,
        # but then keeps track of column with a dictionary. Items in the same column go into
        # same list.
        # Within each column, the order is maintained if we do BFS.

        # IMPORTANT!!!! The number of nodes in the tree is in the range [0, 100].
        if not root:
            return []
        column_dict = defaultdict(list)
        queue = deque([(root, 0)])  # (pointer, col)
        while queue:
            node_t = queue.popleft()
            node = node_t[0]
            col = node_t[1]
            column_dict[col].append(node.val)  # node cannot be null we took care of it above!
            if node.left:
                queue.append((node.left, col - 1))
            # elif node.right:
            if node.right:  # IMPORTANT!!!! NOT elif!!!! DO NOT MAKE THIS MISTAKE!!!!
                queue.append((node.right, col + 1))
        # print(column_dict)
        return [column_dict[key] for key in sorted(column_dict.keys())]

