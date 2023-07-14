from collections import defaultdict
from enum import Enum


class Color(Enum):
    RED = 1,
    BLUE = 0


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Intuition:
        # At the beginning the problem is pretty confusing....
        # But I built a graph myself and it actually worked pretty well.
        # The key is to cover many cases (such as node that goes nowhere, nodes can be reached in multi ways)
        # Example I built is:
        # {
        #    0: [(3, r), (4, b)],
        #    1: [],
        #    2: [(4, r), (1, r)],
        #    3: [(1, r), (1, b)],
        #    4: []
        #}
        # Psudo code:
        # 1. Build graph
        #    redEdges = [[0, 3], [3, 1], [2, 1], [2, 4]], blueEdges = [[3, 1], [3, 2], [0, 4]]
        # 2. BFS and visited from 0 for red => ans_r (note that queue needs to store (node, r/b))
        #    BFS and visited from 0 for blue => ans_b
        # 3. Consolidate ans_r and ans_b take min of each entry
        # UPDATE ^^^^ I REALIZED I DON'T NEED SEPARATE QUEUES, JUST DO BOTH TOGETHER
        # (NODE, EDGE_COLOR) TOGETHER IDENTIFIES UNIQUE PATH IN QUEUE <= EDGE_COLOR IS THE STATE OF THE NODE!

        # 1. Build graph
        # Example:
        # graph = {
        #     0: {Color.RED: [3],
        #         Color.BLUE: [4]},
        #     2: {Color.RED: [1, 4]},
        #     3: {Color.RED: [1],
        #         Color.BLUE: [1, 2]},
        # }  # 1, 4 do not have outgoing edges.
        # In my graph, if a node has no outgoing connection, I do not have it in the graph.
        # But that's ok, because I am using defaultdict, it will automatically create an empty obj.
        # graph = defaultdict(defaultdict(list))  # WRONG!!!!
        graph = defaultdict(lambda: defaultdict(list))  # IMPORTANT!!!!
        for from_node, to_node in redEdges:
            graph[from_node][Color.RED].append(to_node)
        for from_node, to_node in blueEdges:
            graph[from_node][Color.BLUE].append(to_node)
        
        def get_next_color(color: Color):
            # return 1 - color  # 1 -> 0; 0 -> 1  # WRONG!!!!
            return Color.RED if color == Color.BLUE else Color.BLUE

        # BFS from 0
        # queue item contains 3 things (node, color, step) => color is the state RED/BLUE
        # when we pop the item, color==Color.RED means we want to find red neighbor.
        # but when we push the neighbor back to queue, make sure to push with blue.
        ans = [-1] * n
        ans[0] = 0  # 0 to itself is 0
        queue = deque([(0, Color.RED, 0), (0, Color.BLUE, 0)])
        # visited = set((0, Color.RED), (0, Color.BLUE))
        visited = set([(0, Color.RED), (0, Color.BLUE)])
        while queue:
            node, color, step = queue.popleft()
            neighbor_nodes = graph[node][color]
            next_color = get_next_color(color)
            for neighbor_node in neighbor_nodes:
                if (neighbor_node, next_color) not in visited:
                    if ans[neighbor_node] == -1:
                        ans[neighbor_node] = step + 1
                    else:
                        ans[neighbor_node] = min(ans[neighbor_node], step + 1)
                    visited.add((neighbor_node, next_color))
                    queue.append((neighbor_node, next_color, step + 1))
        return ans
        

