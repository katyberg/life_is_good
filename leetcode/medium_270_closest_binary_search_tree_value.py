# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # SOMEBODY HAS THIS SOLUTION!!!!OMG!!!!
    # def closestValue(self, root: TreeNode, target: float) -> int:
    #     closest = root.val
    #     while root:
    #         closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
    #         root = root.left if target < root.val else root.right
    #     return closest 
    # # Above code defines a custom comparison function, when there is a tie, use the item itself.
    # # Example:
    # # people = [
    # #     {'name': 'Alice', 'age': 20},
    # #     {'name': 'Bob', 'age': 20},
    # #     {'name': 'Charlie', 'age': 30}
    # # ]
    # # youngest_person = min(people, key=lambda x: (x['age'], x['name']))
    # # print(youngest_person)  # Outputs: {'name': 'Alice', 'age': 20}

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # New Intuition:
        # In-order traverse the tree and find the boundary values
        inorder = []
        def dfs_inorder(root: Optional[TreeNode], target):
            nonlocal inorder
            if not root:
                return
            if target < root.val:
                dfs_inorder(root.left, target)
            inorder.append(root.val)
            if target > root.val:
                dfs_inorder(root.right, target)
        dfs_inorder(root, target)
        print(f'inorder={inorder}')

        # Go through inorder list, find where target falls within and calculate diff with neighbor
        # inorder should have at least one entry because N => [1, 104]
        if len(inorder) == 1:
            return inorder[0]
        # at least 2 items in inorder now
        if target <= inorder[0]:
            return inorder[0]
        elif target >= inorder[-1]:
            return inorder[-1]
        else:
            for i in range(len(inorder) - 1):
                cur = inorder[i]
                next = inorder[i + 1]
                if target == cur:
                    return cur  # target is closest to itself
                elif cur < target < next:
                    diff1 = abs(target - cur)
                    diff2 = abs(target - next)
                    return cur if diff1 <= diff2 else next  # NOTICE THE <= NOT <
        
        # BELOW IS THE WRONG IMPLEMENTATION!!!!
        # Intuition:
        # Assuming in BST all nodes are different, left < root < right (NO equal condition)
        # 1. Start from root
        # 2. traverse DFS until cannot go anymore
        #    => a. hit null
        #.      b. hit smaller on left or bigger on right
        # 3. calculate min abs value with the node
        # def bs(root: Optional[TreeNode], target: float, parent: Optional[TreeNode]):
        #     if not root:
        #         return parent
        #     if target == root.val:
        #         return root.val
        #     if not root.left and not root.right:  # at leaf node
        #         diff_with_root = abs(target - root.val)
        #         diff_with_parent = abs(target - parent.val)
        #         if diff_with_root == diff_with_parent:
        #             return min(root.val, parent.val) # return smallest if multiple
        #         elif diff_with_root < diff_with_parent:
        #             return root.val
        #         else:
        #             return parent.val
        #         # ^^^^ THIS IS WRONG!!!!!!!!!!!!!!!! BEAUSE WE WANT TO RETURN 4 NOT 2
        #         # (PARENT OF 3) IN THE TEST CASE [4,2,5,1,3] AND TARGET=3.714286
        #     if target < root.val:
        #         return bs(root.left, target, root)
        #     else:  # target > root.val
        #         return bs(root.right, target, root)
        # return bs(root, target, root)  # pass in root as parent of root
            
