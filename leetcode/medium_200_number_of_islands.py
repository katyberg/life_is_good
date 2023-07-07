# My solution has one extra function, the run time is much slower, only beats 6% of people....
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate through all the grid nodes, dfs on its neighbors,
        # mark them as visited as we go.
        # each time we encounter an unvisited node, it's a new island.
        # grid node is represented by (i,j)
        def get_neighbors(i: int, j: int):
            neighbors = []
            # left (same i, j is one less)
            if 1 <= j and 0 <= i <= m - 1: neighbors.append((i, j - 1))
            # right (same i, j is one more)
            if j <= n - 2 and 0 <= i <= m - 1: neighbors.append((i, j + 1))
            # up (same j, i is one less)
            if 1 <= i and 0 <= j <= n - 1: neighbors.append((i - 1, j))
            # down (same j, i is one more)
            if i <= m - 2 and 0 <= j <= n - 1: neighbors.append((i + 1, j))
            print(f'neighbors for i={i} and j={j} ={neighbors}')
            return neighbors

        def dfs(i: int, j: int):
            # set node to visited
            grid[i][j] = '2'
            # go through all neighbors and add each to visited
            neighbors = get_neighbors(i, j)
            for neighbor in neighbors:  # neighbor is a tuple (i, j)
                i, j = neighbor
                # if we encounter land, set it as visited, continue to dfs
                # we ignore '0' (water) and '2' (already visited)
                if grid[i][j] == '1':
                    grid[i][j] = '2'  # set node to visited
                    dfs(i, j)  # visit all its neighbors
        
        # In this implementation, we do not use a visited list, we set visited node to 2.
        m = len(grid)
        n = len(grid[0])  # 1 <= m, n <= 300, grip[0] always exists (could be empty though)
        num_islands = 0
        for i in range(m):
            for j in range(n):
                print(f'i={i}, j={j}, grid[i][j]={grid[i][j]}')
                # if grid[i][j] == 1:  # NOTE THIS IS WRONG, WE HAVE STRING NOT INTEGER!!!!
                if grid[i][j] == '1':
                    num_islands += 1
                    print(f'num_islands={num_islands}')
                    dfs(i, j)  # dfs from this node
        return num_islands
        
# # Output:
# grid =
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# Stdout
# i=0, j=0, grid[i][j]=1
# num_islands=1
# neighbors for i=0 and j=0 =[(0, 1), (1, 0)]
# neighbors for i=0 and j=1 =[(0, 0), (0, 2), (1, 1)]
# neighbors for i=0 and j=2 =[(0, 1), (0, 3), (1, 2)]
# neighbors for i=0 and j=3 =[(0, 2), (0, 4), (1, 3)]
# neighbors for i=1 and j=3 =[(1, 2), (1, 4), (0, 3), (2, 3)]
# neighbors for i=1 and j=1 =[(1, 0), (1, 2), (0, 1), (2, 1)]
# neighbors for i=1 and j=0 =[(1, 1), (0, 0), (2, 0)]
# neighbors for i=2 and j=0 =[(2, 1), (1, 0), (3, 0)]
# neighbors for i=2 and j=1 =[(2, 0), (2, 2), (1, 1), (3, 1)]
# i=0, j=1, grid[i][j]=2
# i=0, j=2, grid[i][j]=2
# i=0, j=3, grid[i][j]=2
# i=0, j=4, grid[i][j]=0
# i=1, j=0, grid[i][j]=2
# i=1, j=1, grid[i][j]=2
# i=1, j=2, grid[i][j]=0
# i=1, j=3, grid[i][j]=2
# i=1, j=4, grid[i][j]=0
# i=2, j=0, grid[i][j]=2
# i=2, j=1, grid[i][j]=2
# i=2, j=2, grid[i][j]=0
# i=2, j=3, grid[i][j]=0
# i=2, j=4, grid[i][j]=0
# i=3, j=0, grid[i][j]=0
# i=3, j=1, grid[i][j]=0
# i=3, j=2, grid[i][j]=0
# i=3, j=3, grid[i][j]=0
# i=3, j=4, grid[i][j]=0

# # I find this solution more succint!
# # Without needing to use a separate neighbors function, it's faster too (beats 88%)
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         count = 0
#         for i in range(m):
#             for j in range(n):
#                 if (grid[i][j] == "1"):
#                     count += 1
#                     self.dfs(grid, i, j, m, n)
#         return count
#    
#     def dfs(self, g, i, j, m, n):
#         if (i < 0 or j < 0 or i >= m or j >= n or g[i][j] == "0"):
#             return
#
#         g[i][j] = "0" # Here we sink the island (Note: only reached when g[i][j] is 1)
#
#         self.dfs(g, i-1, j, m, n)
#         self.dfs(g, i+1, j, m, n)
#         self.dfs(g, i, j-1, m, n)
#         self.dfs(g, i, j+1, m, n)

