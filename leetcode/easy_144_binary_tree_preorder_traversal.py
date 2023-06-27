# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursively
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # # Iteratively
        # answer = []
        # stack = [root]
        # # Note that we add curr_node's right child to the stack first.
        # while stack:
        #     curr_node = stack.pop()
        #     if curr_node:
        #         answer.append(curr_node.val)
        #         stack.append(curr_node.right)  # note that we can just push Null pointer on stack.
        #         stack.append(curr_node.left)  # note that we can just push Null pointer on stack.
        # return answer

        # # Iteratively - REMEMBER WE ARE USING STACK TO MEMORIZE THE POINTER ORDERS!!!!!!!!!!!!!!!!
        # # BELOW IMPLEMENTATION IS WRONG BECAUSE WE NEED TO PUSH RRRRIIIIGGGGHHHHTTTT CHILD FIRST!!!!
        # # WHY IS IT BEING ACCEPTED????
        # stack = [root]
        # result = []
        # while stack:
        #     curr = stack.pop()
        #     result.append(curr.val)
        #     # Below we can also just push a Null pointer
        #     if curr.left:
        #         stack.append(curr.left)  # WRONG!
        #     if curr.right:
        #         stack.append(curr.right)  # WRONG!
        # return result

