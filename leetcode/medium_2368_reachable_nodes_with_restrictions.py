from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # Intuition:
        # edges.length == n - 1 <= this means: no isolated node, no cycle.
        # DFS from 0 to its neighbors
        # keep track of visited AND restricted
        # 1. Build graph
        # 2. Recur on neighbor (but not visited and restricted)
        # Test case:
        # 1. n = 1 (node 0) => 1 (0 is not restricted)
        # 2. Examples given
        
        graph = defaultdict(list)
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
    
        # BELOW EXCEEDS TIME LIMIT WHEN TEST CASE N = 100000....
        # USE visited set JUST TAKES TOO MUCH TIME TO CHECK SET MEMBERSHIP!!!!!!!!!!!!!!!!
        # visited = set()
        # # reachable = []
        # reachable = [0]
        # def dfs(node: int):
        #     if node in visited or node in restricted:
        #         return
        #     visited.add(node)
        #     # reachable.append(node)
        #     reachable[0] += 1
        #     for neighbor in graph[node]:
        #         if neighbor not in visited and neighbor not in restricted:
        #             dfs(neighbor)

        visited = [False] * n
        reachable = [0]
        for node in restricted:
            visited[node] = True
        def dfs(node: int):
            if visited[node]:
                return
            visited[node] = True
            reachable[0] += 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        dfs(0)
        # return len(reachable)
        return reachable[0]

