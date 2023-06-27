# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # Recursively
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        # Iteratively
        # WE NEED 2 STACKS FOR POSTORDER ITERATIVE!
        # THE TWO STACKS BASICALLY HELP REORDER THINGS
        # STACK 1 - (bottom) ROOT -> (pop) -> LEFT -> RIGHT (top)
        # STACK 2 - STORE THE NODES IN SEQUENCE OF POPPING OFF LATER 
        #           (bottom) ROOT -> RIGHT -> LEFT (top) <= pop LEFT -> RIGHT -> ROOT
        if not root:
            return []
        result = []
        stack1 = [root]
        stack2 = []
        while stack1:
            curr = stack1.pop()
            stack2.append(curr)
            if curr.left: stack1.append(curr.left)  # left needs to go first
            if curr.right: stack1.append(curr.right)
        # now we are ready to pop things off stack 2 for result
        while stack2:
            result.append(stack2.pop().val)
        return result
    
        # # Iteratively - this is solution provided by Leetcode
        # # Basically same idea, since Stack2 is really just a list, just return it in reverse
        # if root is None:
        #     return []
        # stack, output = [root, ], []
        # while stack:
        #     root = stack.pop()
        #     output.append(root.val)
        #     if root.left is not None:
        #         stack.append(root.left)
        #     if root.right is not None:
        #         stack.append(root.right)
        # return output[::-1]

