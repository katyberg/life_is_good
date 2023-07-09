from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Intuition:
        # 1. Build graph as adjacency list
        # 2. Start from source, dfs
        #    return whether subtree can reach destination
        #    base case: False if node is null, True if destination is reached
        # Q: It is not clear when I have a single node, what happens?
        #    Confligt requirement - n >= 1, but u != v, what happens when I have only one node?
        #    That means I will have edges=[[]] and graph = {0: []} (0 could be something else)
        #    because 1 <= n....?
        # Test case:
        # [], source=? destination=? <= they are the same then? Should I return True?
        # [[1,2]], source=1 destination=2 (or source=1 destination=3, source=2 destination=3)
        # Test cases provided by examples.
        
        # FOUND someone with this precondition check, which I like (answered my question above).
        if len(edges) <= 0 or n == 1 or [source,destination] in edges:
            return True
        
        # Build graph as adjacency list
        graph = defaultdict(list)
        for edge in edges:
            s, d = edge
            graph[s].append(d)
            graph[d].append(s)
        # print(f'graph={graph}')
        
        # DFS from source node
        # dfs returns True if destination can be reached by source
        visited = set()
        def dfs(source: int, destination: int):
            visited.add(source)  # put source node in visited as soon as recur
            # print(f'dfs({source}, {destination}) is called. ')
            # print(f'{source} added to visited. visited={visited}')
            # IMPORTANT!!!! THIS BASE CASE DOES NOT EXIST!!!!
            # WHEN SOURCE=0 THIS WOULD NOT EXECUTE ANYMORE AND RESULT IN WRONG ANSWER!!!!!!!!!!!!!!!!
            # if not source:
            #     return False
            if source == destination:
                return True
            neighbors = graph[source]
            # print(f'source {source} has neighbors={neighbors}')
            found = False
            for neighbor in neighbors:
                if found:  # if found in one neighbor we can break out and return
                    break
                if neighbor not in visited:
                    found = dfs(neighbor, destination)
            return found
        return dfs(source, destination)
