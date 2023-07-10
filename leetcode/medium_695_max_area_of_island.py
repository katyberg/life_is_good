class Solution:
    def __init__(self):
        self.max_area = float('-inf')

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Intuition:
        # This is a graph given in a form of a matrix (1 represents a node)
        # Traverse row by row, column by column, keep track of visited node.
        # every time I hit a unvisited node, it's a new connected component;
        # then I start counting the number of nodes in it.
        # How to count? go up/down/left/right, if not (visited or 0) increment by 1.
        # keep track of max count, return at the end.
        # Note I will set a node to 2 if it's visited
        
        # 1 <= m, n <= 50
        m = len(grid)     # m is the number of rows
        n = len(grid[0])  # n is the number of columns
        
        # for i in range(m):
        #     print(grid[i])
        
        def dfs(row: int, col: int):  # (row, col) is the coordinate of a node
            # print(f'dfs(row={row}, col={col})')
            if grid[row][col] == 0 or grid[row][col] == 2:
                return 0
            grid[row][col] = 2  # 2 means visited
            # left: grid[row][col - 1]
            # right: grid[row][col + 1]
            # up: grid[row - 1][col]
            # down: grid[row + 1][col]
            left = right = up = down = 0
            if col > 0 and grid[row][col - 1] == 1: left = dfs(row, col - 1)
            if col < n - 1 and grid[row][col + 1] == 1: right = dfs(row, col + 1)
            if row > 0 and grid[row - 1][col] == 1: up = dfs(row - 1, col)
            if row < m - 1 and grid[row + 1][col] == 1: down = dfs(row + 1, col)
            total = 1 + left + right + up + down
            # print(f'total={total}')
            return total

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    # print(f'area when recurring on ({row}, {col}) is {area}')
                    self.max_area = max(self.max_area, area)
                    # print(f'self.max_area={self.max_area}')

        # IMPORTANT!!!! DO NOT REUTRN float('-inf') if there is no 1!!!!
        # Remember to run through all test cases: test case grid = [[0,0,0,0,0,0,0,0]]
        return self.max_area if self.max_area != float('-inf') else 0
