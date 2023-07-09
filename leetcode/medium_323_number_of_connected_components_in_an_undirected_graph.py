from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Intuition
        # 1. Build undirected graph using edges
        # 2. Loop through all the nodes (not from keys of graph but directly from 0 - n-1
        #     (because a node that does not connect to any other node would not exist in the edges
        #     dfs to find all the nodes that are connected to it (maintaining visited)
        #     whenever I encounter a note not in visited, it’s the beginning of a new 
        #     connected component
        # Test cases:
        # n = 1
        # 0,1 not connected (this cannot be because 1 <= edges.length <= 5000)
        # 0,1 connected edges=[[0,1]]
        # Examples provided by the problem

        graph = defaultdict(list)
        for edge in edges:
            x, y = edge
            graph[x].append(y)
            graph[y].append(x)

        num_connected_component = 0
        visited = set()
        def dfs(node: int):
            visited.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
             if node not in visited:
                num_connected_component += 1
                dfs(node)

        return num_connected_component 

