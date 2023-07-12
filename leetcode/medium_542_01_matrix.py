class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # The key is to start from 0
        # because 0 takes 0 step to get to 0, so if 1 is very sparse,
        # this algorithm would run much faster....
        # (Who would have thought of that....!!!!)

        # First go through the matrix to find all the zeros, put it in queue
        m = len(mat)
        n = len(mat[0])  # 1 <= m, n <= 104
        queue = deque()
        visited = set()  # IMPORTANT!!!! Each 0 added to the queue is immediately visited!!!!
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))  # start with 1
                    visited.add((row, col))# IMPORTANT!!!!

        # Then go through queue to do BFS and update matrix
        def get_neighbors(row, col):
            neighbors = []
            # left
            if col > 0: neighbors.append((row, col - 1))
            # right
            if col < n - 1: neighbors.append((row, col + 1))
            # up
            if row > 0: neighbors.append((row - 1, col))
            # down
            if row < m - 1: neighbors.append((row + 1, col))
            return neighbors  # returns [(a, b), (c, d)....] never out of bounds

        while queue:
            row, col, step = queue.popleft()
            neighbors = get_neighbors(row, col)
            for neighbor in neighbors:
                if neighbor not in visited:
                    # at this point, we will only encounter 1 because all 0 are visited already
                    visited.add(neighbor)
                    neighbor_row, neighbor_col = neighbor
                    mat[neighbor_row][neighbor_col] = step
                    queue.append((neighbor_row, neighbor_col, step + 1))
                        
        return mat

