# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # IMPORTANT about this problem is from target we need to go UP as well!!!!
        # In the example [3,5,1,6,2,0,8,null,null,7,4] k=2, "1" is part of the answer too!
        # Because of such, we have to convert the tree to a bi-directional graph first!!!!
        # we can perform a DFS or BFS for that.
        # Test case:
        # 1. tree=[1], target=1, k=3
        # 2. tree=[1,2], target=2, k=3
        # 3. examples provided in problem

        # First we build the graph
        graph = defaultdict(list)

        # # DFS Pre-order Implementation:
        # def dfs(root: TreeNode):
        #     if not root:
        #         return
        #     left = root.left
        #     right = root.right
        #     if left:
        #         graph[root.val].append(left.val)
        #         graph[left.val].append(root.val)
        #     if right:
        #         graph[root.val].append(right.val)
        #         graph[right.val].append(root.val)
        #     dfs(left)
        #     dfs(right)
        # dfs(root)

        # BFS Implementation:
        queue_for_graph = deque()
        queue_for_graph.append(root)
        while queue_for_graph:
            root = queue_for_graph.popleft()
            if root:  # n has range [1, 500], but still good to be defensive.
                left = root.left
                right = root.right
            if left:
                graph[root.val].append(left.val)
                graph[left.val].append(root.val)
                queue_for_graph.append(left)
            if right:
                graph[root.val].append(right.val)
                graph[right.val].append(root.val)
                queue_for_graph.append(right)
        print(graph)
        # graph = {
        #   3: [5, 1], 
        #   5: [3, 6, 2], 
        #   1: [3, 0, 8], 
        #   6: [5], 
        #   2: [5, 7, 4], 
        #   7: [2], 
        #   4: [2], 
        #   0: [1], 
        #   8: [1]
        # }

        # Now we do BFS from target node to find all nodes within k distance
        visited = set()
        queue = deque()
        # queue.append(target)  # BE CAREFUL!!!! DO NOT MIX POINTER AND INTEGER!!!!
        queue.append(target.val)
        visited.add(target.val)
        for i in range(k):
            layer_size = len(queue)
            # print(f'iteration i={i} layer_size={layer_size} queue={queue}')
            for j in range(layer_size):
                # print(f'iteration j={j}; queue={queue}')
                node = queue.popleft()
                # print(f'popped {node} queue={queue}')
                neighbors = graph[node]
                # print(f'neighbors of {node}={neighbors}')
                for neighbor in neighbors:
                    if neighbor != target.val and neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)  # DO NOT VISIT SAME NODE TWICE!!!!
        print(queue)
        return list(queue)

# OUTPUT
# defaultdict(<class 'list'>, {3: [5, 1], 5: [3, 6, 2], 1: [3, 0, 8], 6: [5],
#                              2: [5, 7, 4], 0: [1], 8: [1], 7: [2], 4: [2]})
# iteration i=0 layer_size=1 queue=deque([5])
# iteration j=0; queue=deque([5])
# popped 5 queue=deque([])
# neighbors of 5=[3, 6, 2]
# iteration i=1 layer_size=3 queue=deque([3, 6, 2])
# iteration j=0; queue=deque([3, 6, 2])
# popped 3 queue=deque([6, 2])
# neighbors of 3=[5, 1]
# iteration j=1; queue=deque([6, 2, 1])
# popped 6 queue=deque([2, 1])
# neighbors of 6=[5]
# iteration j=2; queue=deque([2, 1])
# popped 2 queue=deque([1])
# neighbors of 2=[5, 7, 4]
# deque([1, 7, 4])
