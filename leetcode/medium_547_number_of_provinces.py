from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Example:
        # isConnected = [[1,2],[0,2],[0,1,3],[]]
        # Adjacency Matrix:
        # isConnected = 
        # [[1,1,1,0],
        #  [1,1,1,0],
        #  [1,1,1,1],
        #  [0,0,1,1]]
        # Graph:
        # graph = 
        # {
        #   0: [1,2],
        #   1: [0,2],
        #   2: [0,1,3],
        #   3: 
        # }

        # DFS
        # the point of traversal in this problem is just to add a node encountered to seen.
        # ps: inner function can access graph and seen just fine
        def dfs(node: int):
            for neighbor in graph[node]:
                # NOTE THAT IT IS VERY IMPORTANT TO CHECK seen FIRST!!!!
                # OTHERWISE WE WILL BE TRAVERSASING WAY TOO MANY TIMES UNNECESSARILY!!!!
                if neighbor not in seen:
                    seen.add(neighbor)  # we first add neighbor to seen
                    dfs(neighbor)

        # Build the graph (dict of list) per adjacency matrix
# PS: J starts with N+1 ONLY WORKS FOR THIS PROBLEM, SEE GOOGLE DOC FOR A GRAPH I MADE ABOUT IT!
# https://docs.google.com/document/d/1QVQHwMknDe6saq0RJGqLLEHb_L4UWX0pa_Mnk6E_njI/edit?usp=sharing
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    # undirected graph, edge goes both directions
                    graph[i].append(j)
                    graph[j].append(i)
        print(graph)

 # WE HAVE TO ITERATE THROUGH ALL i, BECAUSE NODE THAT IS NOT CONNECTED TO ANY NODE 
 # WILL NOT EXIST IN THE GRAPH WE CREATED ABOVE!!!!!!!!!!!!!!!!
 # Example:
 # connected = [[1,1,0],[1,1,0],[0,0,1]] => graph={0:[1], 1:[0]} NOTE 2 is NOT in here!!!!
        seen = set()
        num_connected_component = 0
        for i in range(n):
            if i not in seen:
                num_connected_component += 1
                seen.add(i)
                dfs(i)
        return num_connected_component

        # IMPORTANT!!!! BELOW IS WRONG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # WE CANNOT ITERATE THROUGH GRAPH!!!! HAVE TO ITERATE THROUGH isConnected INDEX!!!!
        # BECAUSE IN A GRAPH WITH MULTIPLE CONNECTED COMPONENTS, THE GRAPH WE CONSTRUCT ABOVE
        # ONLY CONTAIN THE CONNECTED ONES ONLY BECAUSE J STARTS WITH I+1 !!!!!!!!!!!!!!!!
        # # Identify connected component:
        # # Start from a random node (first node), each time we pick up a node, 
        # # if it has not been seen before, it's the first node we encounter 
        # # in a new connected component.
        # seen = set()
        # num_connected_component = 0
        # for node in graph:
        #     if node not in seen:
        #         num_connected_component += 1
        #         seen.add(node)  # we first add node to seen
        #         dfs(node)
        # return num_connected_component


# # Also I find this solution straight-forward!!!! It does not even build graph!!!!
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         visited = set()
#         ans = 0
#         def dfs(i):
#             visited.add(i)
#             for j, connected in enumerate(isConnected[i]):
#                 if j not in visited and connected:
#                     dfs(j)
#         for i, row in enumerate(isConnected):
#             if i not in visited:
#                 dfs(i)
#                 ans += 1
#         return ans

