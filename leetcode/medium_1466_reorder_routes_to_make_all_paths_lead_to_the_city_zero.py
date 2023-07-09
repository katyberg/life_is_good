from collections import defaultdict
class Solution:
    # I SAW THE SOLUTION THERE IS A TRICK!!!!
    # ONCE I LEARNT ABOUT THE TRICK, IT BECOMES SO EASY!!!!
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Build the graph UN-DIRECTED
        # Example: go through connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        #          build undirected graph which should look like this:
        # graph = {
        #     0: [1, 4],  # (0, 1), (0, 4)
        #     1: [0, 3],  # (1, 0), (1, 3)
        #     2: [3],     # (2, 3)
        #     3: [1, 2],  # (3, 1), (3, 2)
        #     4: [0, 5],  # (4, 0), (4, 5)
        #     5: [4]      # (5, 4)
        # }
        # For every pair (x, y), the valid connection should be from y to x or (y, x)
        # so if we see (x, y) in the graph, it's an edge that needs to be flipped;
        # we can start from capital 0, and visit all its neighbors outwards;
        # each time we encounter the (x, y) connection in the connections array,
        # we increment the number of edges that need to be flipped.
        # We then recur and do the same for all its neighbors, we need to maintain
        # visited along the way and do not visit a node twice during recursion!
        graph = defaultdict(list)
        orig_connections = set()
        for (x, y) in connections:
            graph[x].append(y)
            graph[y].append(x)
            # convert orig list into set of tuples for ease of comparison later
            orig_connections.add((x, y))
        print(f'graph={graph}')
        print(f'orig_connections={orig_connections}')
        print('=================')
        
        visited = set()
        num_connection_flipped = 0
        def dfs(city: int):
            nonlocal num_connection_flipped  # NOTE WE NEED THIS OTHERWISE UnboundLocalError
            # Below block is not needed because we never recur on visited city
            # if city in visited:
            #     print(f'city {city} is in visited ({visited}), returning....')
            #     return
            visited.add(city)
            # print(f'dfs({city}) is called, visited={visited}')
            neighbors = graph[city]
            # print(f'neighbors of {city} are: {neighbors}')
            for neighbor in neighbors:
                # BELOW CHECKING IS VERY IMPORTANT!!!!!!!!!!!!!!!!
                # I ORIGINALLY DID NOT HAVE THIS CHECK AND HAD WRONG ANSWER!!!!
                # IN TERMS OF RECURRING ON NEIGHBORS, WE NEVER GO BACKWARDS!!!!
                # IF WE GO BACKWARDS WE WILL CONSIDER (4,0) A BAD CONNECTION BELOW AND GOT WRONG ANSWER!!!!
                if neighbor not in visited:
                    # (city, neighbor) is what we DO NOT WANT! We want (neighbor, city).
                    # (neighbor, city) means there is a connection from neighbor to city.
                    if (city, neighbor) in orig_connections:
                        num_connection_flipped += 1
                        # print(f'Found {(city, neighbor)} in orig_connections, num_connection_flipped={num_connection_flipped}')
                    dfs(neighbor)
                # else:
                #     print(f'neighbor {neighbor} is in visited ({visited}), skipping...')
        dfs(0)
        return num_connection_flipped

# Output of above code:
# graph=defaultdict(<class 'list'>, {0: [1, 4], 1: [0, 3], 3: [1, 2], 2: [3], 4: [0, 5], 5: [4]})
# orig_connections={(0, 1), (4, 0), (2, 3), (4, 5), (1, 3)}
# =================
# dfs(0) is called, visited={0}
# neighbors of 0 are: [1, 4]
# Found (0, 1) in orig_connections, num_connection_flipped=1
# dfs(1) is called, visited={0, 1}
# neighbors of 1 are: [0, 3]
# neighbor 0 is in visited ({0, 1}), skipping...
# Found (1, 3) in orig_connections, num_connection_flipped=2
# dfs(3) is called, visited={0, 1, 3}
# neighbors of 3 are: [1, 2]
# neighbor 1 is in visited ({0, 1, 3}), skipping...
# dfs(2) is called, visited={0, 1, 2, 3}
# neighbors of 2 are: [3]
# neighbor 3 is in visited ({0, 1, 2, 3}), skipping...
# dfs(4) is called, visited={0, 1, 2, 3, 4}
# neighbors of 4 are: [0, 5]
# neighbor 0 is in visited ({0, 1, 2, 3, 4}), skipping...
# Found (4, 5) in orig_connections, num_connection_flipped=3
# dfs(5) is called, visited={0, 1, 2, 3, 4, 5}
# neighbors of 5 are: [4]
# neighbor 4 is in visited ({0, 1, 2, 3, 4, 5}), skipping...

    # # Also I like this solution others have: Very clear!!!!
    # # Again, the trick is to have the undirected graph first!!!!
    # # Also, it's using an array to represent visited which is faster!!!!
    # def minReorder(self, n: int, connections: List[List[int]]) -> int:
    #     adjacency = [[] for _ in range(n)]
    #     reverse_adjacency = [[] for _ in range(n)]
    #     for source, target in connections:
    #         adjacency[source].append(target)
    #         reverse_adjacency[target].append(source)
    #     visited = [False] * n
    #     visited[0] = True
    #     ans = 0
    #     queue = deque([0])
    #     while queue:
    #         source = queue.popleft()
    #         for target in reverse_adjacency[source]:
    #             if not visited[target]:
    #                 visited[target] = True
    #                 queue.append(target)
    #         for target in adjacency[source]:
    #             if not visited[target]:
    #                 ans += 1
    #                 visited[target] = True
    #                 queue.append(target)
    #     return ans


    # # BELOW WAS MY FIRST TRY AND IT DID NOT WORK!!!!
    # # AFTER LOOKING AT SOLUTION, THERE IS A TRICK, ONCE REALIZED THIS TRICK, IT BECOMES VERY EASY....
    # def minReorder(self, n: int, connections: List[List[int]]) -> int:
    #     # Intuition:
    #     # Build graph (adjacency list)
    #     # Start from node 0 (capital city), dfs
    #     # each time we find a connection in wrong direction, reverse it
    #     # (wrong connection means the node we have is not 2nd in list)

    #     def dfs(city):
    #         if city in visited:
    #             return
    #         visited.append(city)
    #         neighbors = graph[city]
    #         for neighbor in neighbors:
    #             graph[city].remove(neighbor)
    #             graph[neighbor].append(city)
    #             num_reversed += 1
    #             dfs(neighbor)
    #            
    #     visited = set()
    #     # Build graph
    #     # For example: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    #     # graph = {
    #     #   0: [1],
    #     #   1: [3],
    #     #   2: [3],
    #     #   4: [0, 5]
    #     # }
    #     graph = defaultdict(list)
    #     for connection in connections:
    #         from_city = connection[0]
    #         to_city = connection[1]
    #         graph[from_city].append(to_city)
    #    
    #     # go through all cities, if it's not pointing to 0 or its decendent, reverse it
    #     num_reversed = 0
    #     for city in range(len(n)):
    #         if city not in visited:
    #             # visited.append(city)
    #             dfs(city)

