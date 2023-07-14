class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Intuition:
        # This is the same BFS shortest path problem except there are many different end points
        # so when I check end point, I need to check a few - we should build end points array first.
        # Ps: I started with building a little more complicated use case and realized it's not needed.
        # Psudo code:
        # 1. Start with entrance, BFS in 4 directions
        # 2. Loop through queue
        #    - pop node
        #    - Get legit neighbors
        #    - For each neighbor:
        #        - check if reached end point then return
        #        - update visited (row, col) and add to queue (row, col, step)
        # 3. return -1 if did not encounter an exit

        EMPTY = '.'
        WALL = '+'
        m = len(maze)
        n = len(maze[0])  # 1 <= m, n <= 100

        def get_exit_nodes(maze: List[List[str]]):
            exit_nodes = set()
            # first row (row=0), last row (row = m - 1) 
            for col in range(n):
                if maze[0][col] == EMPTY: exit_nodes.add((0, col))
                if maze[m - 1][col] == EMPTY: exit_nodes.add((m - 1, col))
            # first col (col = 0), last col (col = n - 1)
            for row in range(m):
                if maze[row][0] == EMPTY: exit_nodes.add((row, 0))
                if maze[row][n - 1] == EMPTY: exit_nodes.add((row, n - 1))
            # NOTE discard does NOT throw exception but remove does!!!!
            exit_nodes.discard((entrance[0], entrance[1]))  # entrance cannot be exit
            return exit_nodes
        
        # Only returns legit neighbors of the node at (row, col)
        # legit - within bounds (could contain exit node(s))
        def get_neighbors(row: int, col: int):
            neighbors = []
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # left, right, up, down
            for row_offset, col_offset in directions:
                new_row, new_col = row + row_offset, col + col_offset
                if 0 <= new_row <= m - 1 and 0 <= new_col <= n - 1 and maze[new_row][new_col] != WALL:
                    neighbors.append((new_row, new_col))
            return neighbors
        
        exit_nodes = get_exit_nodes(maze)
        if not exit_nodes:
            return -1

        entrance_row, entrance_col = entrance[0], entrance[1]
        queue = deque([(entrance_row, entrance_col, 0)])  # entry in queue (row, col, step)
        visited = set((entrance_row, entrance_col))
        while queue:
            row, col, step = queue.popleft()
            neighbors = get_neighbors(row, col)
            for neighbor in neighbors:
                if neighbor not in visited:
                    if neighbor in exit_nodes:
                        return step + 1
                    visited.add(neighbor)
                    neighbor_row, neighbor_col = neighbor
                    queue.append((neighbor_row, neighbor_col, step + 1))
        return -1

