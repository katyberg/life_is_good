############################################################################
# TRY # 2 
############################################################################
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])  # 1 <= m, n <= 40
        def get_neighbors(row: int, col: int, num_obstacle_eliminated: int):
            neighbors = []
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # right, down, up, left
            for direction in directions:
                row_diff, col_diff = direction
                new_row = row + row_diff
                new_col = col + col_diff
                if 0 <= new_row <= m - 1 and 0 <= new_col <= n - 1:  # not out of bounds
                    if grid[new_row][new_col] == 1:
                        if num_obstacle_eliminated < k and (new_row, new_col, num_obstacle_eliminated + 1) not in visited:
                           neighbors.append((new_row, new_col, num_obstacle_eliminated + 1))
                    else:  # 0
                        if (new_row, new_col, num_obstacle_eliminated) not in visited:
                            neighbors.append((new_row, new_col, num_obstacle_eliminated))
            return neighbors

        # Start BFS traversing cell with 0
        # When encountering 1, treat it as 0 k times
        # Keep updating the depth as we go until we reach the end (start with 1)
        # Note: grid[0][0] == grid[m - 1][n - 1] == 0

        # IMPORTANT!!!! NEED TO TAKE CARE OF BASE CASE!!!!
        # TEST CASE [[0]] WILL RETURN -1 WITH OUR ALGORITHM OTHERWISE!!!!
        # NOTE grid[0][0] == grid[m - 1][n - 1] == 0
        if m == 1 and n == 1 and grid[0][0] == 0:
            return 0

        visited = set()
        # the third element represents num of obstacle elinimation used to get to this cell
        # we need the first 3 elements to be tracked in visited
        # the fourth element is storing the total steps
        queue = deque([(0, 0, 0, 0)])
        visited.add((0, 0, 0))
        while queue:
            row, col, num_obstacle_eliminated, step = queue.popleft()
            # print(f'popped: ({row}, {col}, {num_obstacle_eliminated}, step={step}), queue={queue}')
            # if we have reached the destination, just return step
            if row == m - 1 and col == n - 1:
                return step
            neighbors = get_neighbors(row, col, num_obstacle_eliminated)
            # print(f'neighbors={neighbors}')
            for neighbor in neighbors:
                neighbor_row, neighbor_col, neighbor_num_obstacle_eliminated = neighbor
                # immediately set neighbor as visited before adding to queue
                visited.add((neighbor_row, neighbor_col, neighbor_num_obstacle_eliminated))
                queue.append((neighbor_row, neighbor_col, neighbor_num_obstacle_eliminated, step + 1))
            # print(f'====> queue={queue}')
        return -1  # never reached the destination


# ############################################################################
# # TRY # 1 (good implementation but got wrong answer for some test cases)
# ############################################################################
# # Below solution is WRONG for some of the test cases!!!!
# # Remember, the key is, in addition to regular binary matrix BFS traversal, 
# # the VISITED entry needs to contain a 3rd element - # of obstacle elimination performed up to this point.
# # First of all, for a given cell, all paths that arrive at this cell
# #  with a certain number of obstacle elimination are considered the same.
# # But if I reach a cell with a different number of obstacle elimination paths, they are considered different.
# # Therefore, I cannot use a simple VISITED array like we had done in the past. 
# # The VISITED needs to store (a, b, 0), (a, b, 1), etc, for (a, b) 
# # because those are considered different paths. Without the 3rd element, 
# # I would have skipped many other possibility therefore come to the wrong conclusions.
# # Test case that failed:
# # [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],
# #  [0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],
# #  [0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]
# #  Output: 26
# #  Expected: 20
# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         # Intuition:
#         # This is the same problem as 1091. Shortest Path in Binary Matrix 
#         # https://leetcode.com/problems/shortest-path-in-binary-matrix/
#         # except removing 1's k times
#
#         m = len(grid)
#         n = len(grid[0])  # 1 <= m, n <= 40
#
#         # Define get_neighbors function
#         # get_neighbors returns ONLY useful neighbors (not obstacle, not visited)
#         # However, obstacle will be turned into useful cell with k iterations!
#         num_obstacle_removed = 0
#         def get_neighbors(row: int, col: int):
#             nonlocal num_obstacle_removed  # REMEMBER TO DECLARE nonlocal!!!!!!!!
#             neighbors = []
#             # directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # left, right, up, down
#             # Try right, down, up, left => give right, down preference because closer to end, but STILL wrong!!!!
#             directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
#             for direction in directions:
#                 row_diff, col_diff = direction
#                 new_row = row + row_diff
#                 new_col = col + col_diff
#                 # IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                 # SINCE new_row and new_col ARE ALREADY CALCULATED, IT NEEDS TO HAVE <=!!!!!!!!
#                 # if 0 < new_row < m - 1 and 0 < new_col < n - 1:
#                 if 0 <= new_row <= m - 1 and 0 <= new_col <= n - 1:
#                     print(f'---- considering ({new_row}, {new_col}), grid[new_row][new_col]={grid[new_row][new_col]}')
#                     if grid[new_row][new_col] == 1 and num_obstacle_removed < k:
#                         num_obstacle_removed += 1
#                         print(f'Removed obstacle ({new_row}, {new_col}) num_obstacle_removed={num_obstacle_removed}')
#                         neighbors.append((new_row, new_col))
#                     elif grid[new_row][new_col] == 0:
#                         neighbors.append((new_row, new_col))
#                     # ignore anything other than 1 and 0
#             return neighbors
#
#         # Start BFS traversing cell with 0
#         # When encountering 1, treat it as 0 k times
#         # Keep updating the depth as we go until we reach the end (start with 1)
#         # Note: grid[0][0] == grid[m - 1][n - 1] == 0
#
#         # IMPORTANT!!!! NEED TO TAKE CARE OF BASE CASE!!!!
#         # TEST CASE [[0]] WILL RETURN -1 WITH OUR ALGORITHM OTHERWISE!!!!
#         # NOTE grid[0][0] == grid[m - 1][n - 1] == 0
#         if m == 1 and n == 1 and grid[0][0] == 0:
#             return 0
#        
#         queue = deque([(0, 0)])
#         # grid[0][0] = 1  # This 1 serves two purposes: mark visited and also keep track of steps
#         # 1 DOES NOT WORK!!!! BECAUSE (0, 0) WILL BE CONSIDERED AS A NEIGHBOR WHICH IS WRONG!!!!
#         grid[0][0] = 2 
#         while queue:
#             row, col = queue.popleft()
#             step = grid[row][col]
#             print(f'popped: ({row}, {col}), step={step}, queue={queue}')
#             neighbors = get_neighbors(row, col)
#             print(f'neighbors={neighbors}')
#             for neighbor in neighbors:
#                 neighbor_row, neighbor_col = neighbor
#                 # if we have reached the destination, just return step
#                 if neighbor_row == m - 1 and neighbor_col == n - 1:
#                     # return step
#                     return step - 1  # SEE IMPORTANT ABOVE, WE START WITH 2 SO REDUCE 1 HERE!!!!
#                 # immediately set neighbor as visited before adding to queue
#                 grid[neighbor_row][neighbor_col] = step + 1
#                 queue.append((neighbor_row, neighbor_col))
#             print(f'====> queue={queue}')
#         return -1  # never reached the destination
#
#         # Output:
#         # popped: (0, 0), step=2, queue=deque([])
#         # ---- considering (0, 1), grid[new_row][new_col]=0
#         # ---- considering (1, 0), grid[new_row][new_col]=1
#         # Removed obstacle (1, 0) num_obstacle_removed=1
#         # neighbors=[(0, 1), (1, 0)]
#         # ====> queue=deque([(0, 1), (1, 0)])
#         # popped: (0, 1), step=3, queue=deque([(1, 0)])
#         # ---- considering (0, 0), grid[new_row][new_col]=2
#         # ---- considering (0, 2), grid[new_row][new_col]=0
#         # ---- considering (1, 1), grid[new_row][new_col]=1
#         # neighbors=[(0, 2)]
#         # ====> queue=deque([(1, 0), (0, 2)])
#         # popped: (1, 0), step=3, queue=deque([(0, 2)])
#         # ---- considering (1, 1), grid[new_row][new_col]=1
#         # ---- considering (0, 0), grid[new_row][new_col]=2
#         # ---- considering (2, 0), grid[new_row][new_col]=0
#         # neighbors=[(2, 0)]

