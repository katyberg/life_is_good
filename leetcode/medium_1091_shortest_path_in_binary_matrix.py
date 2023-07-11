from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # I read the Edtorial document, it is REALLY GOOD!
        # First write psudo code:
        #     create queue, push (0, 0) in queue (but if [0][0] is not 0 return -1 already)
        #     while queue is not empty:
        #         deque cell  # note is represeneted by (row, col)
        #         set cell (grid[row][col]) to current depth + 1
        #         get neighbors
        #         # ^ will have separate function for it,
        #         # neighbor is 8 direction in bound that is 0
        #         # (visited will have depth already, blocked will have 1)
        #         iterate over neighbors
        #         if neighbor is end cell
        #             return current depth + 1
        #             # ^ this is potentially faster than checking in outer loop
        #         enqueue neighbor

        def get_neighbors(row: int, col: int):
            directions = [
                (-1, -1),  # left up
                (0, -1),   # left
                (1, -1),   # left down
                (-1, 0),   # up
                (1, 0),    # down
                (-1, 1),   # right up
                (0, 1),    # right
                (1, 1),    # right down
            ]
            neighbors = []
            for direction in directions:
                row_offset, col_offset = direction
                new_row = row + row_offset
                new_col = col + col_offset
                # if grid[new_row][new_col] is not 0, it's either visited (depth) or blocked (1)
                if 0 <= new_row <= n - 1 and 0 <= new_col <= n - 1 and grid[new_row][new_col] == 0:
                    neighbors.append((new_row, new_col))
            return neighbors
        # Ps: Can convert above function to yield
        # def get_neighbours(row, col):
        #     for row_difference, col_difference in directions:
        #         new_row = row + row_difference
        #         new_col = col + col_difference
        #         if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
        #             continue
        #         if grid[new_row][new_col] != 0:
        #             continue
        #         yield (new_row, new_col)
        
        n = len(grid)  # grid is n x n matrix
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        
        # # Version 1 => modify the matrix as we go; get_neighbors can remain as is.
        # # queue = deque((0, 0))  # NOTE THIS IS WRONG!!!! HAS TO BE A LIST!!!!
        # queue = deque([(0, 0)])  # cell is represented by (row, col) tuple, grid[0][0] has to be 0
        # # Ps: I could also just do:
        # # queue = deque()
        # # queue.append((0, 0))
        # grid[0][0] = 1  # IMPORTANT: mark cell at (0, 0) to have depth 1 (also indicates visited)
        # while queue:
        #     row, col = queue.popleft()  # NOTE we have to put (row, col) in tuple here!
        #     cur_depth = grid[row][col]  # IMPORTANT HOW cur_depth IS SET/INCREMENTED!!!!
        #     if row == n - 1 and col == n - 1:
        #         return cur_depth
        #     neighbors = get_neighbors(row, col)  # return only neighbor that we should work on
        #     print(f'row={row}, col={col}, cur_depth={cur_depth}, neighbors={neighbors}')
        #     for neighbor in neighbors:
        #         # IMPORTANT!!!! BELOW STRATEGY FAILED TEST CASE [[0]]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #         # PUT THIS CHECK AT THE BEGINNING OF EACH RECURRENCE WORKS BETTER!!!!
        #         # # we preemptively check neighbor before recurring, could be faster
        #         # if neighbor == (n - 1, n - 1):  # we guarenteed that first and last cell has 0
        #         #     return cur_depth + 1
        #         neighbor_row, neighbor_col = neighbor
        #         grid[neighbor_row][neighbor_col] = cur_depth + 1
        #         queue.append(neighbor)
        
        # Version 2 => cannot modify the matrix itself; get_neighbors can remain as is.
        queue = deque([(0, 0, 1)])  # row, col, depth (which starts at 1)
        to_explore = set()
        while queue:
            row, col, depth = queue.popleft()
            # IMPORTANT!!!! THIS IS WRONG PLACE TO PUT visited!!!! IN FACT THE NAME VISITED IS CONFUSING TO BEGIN WITH!
            # WE SHOULD UPDATE visited BEFORE PUTTING A NODE ON THE STACK OR QUEUE TO BEGIN WITH!!!!
            # THAT'S WHY I CHANGE THE NAME TO to_explore.
            # IN THE STACK DFS RECURSION IMPLEMENTATION, IT JUST SO HAPPEN THAT IT DOES NOT MATTER IF WE PUT IT AS
            # THE FIRST LINE OF RECURSIVE CALL (BECAUSE NOTHING ELSE HAPPENS IN BETWEEN). SEE EXAMPLE:
            # https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/editorial/
            # visited.add((row, col))
            if row == n - 1 and col == n - 1:
                return depth
            neighbors = get_neighbors(row, col)
            for neighbor in neighbors:
                if neighbor not in to_explore:
                    neighbor_row, neighbor_col = neighbor
                    to_explore.add((neighbor_row, neighbor_col))
                    queue.append((neighbor_row, neighbor_col, depth + 1))
        return -1

