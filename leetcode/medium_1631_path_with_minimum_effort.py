class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Test case:
        # [3]

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        # Return True if a path exists with effort from (0, 0) to (m, n)
        # DFS to see if a path exist => use stack and visited
        def successful(effort: int):
            stack = [(0, 0)]
            visited = set((0, 0))
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # left, right, up, down
            while stack:
                row, col = stack.pop()
                if (row, col) == (m - 1, n - 1):
                    return True
                for dx, dy in directions:
                    next_row, next_col = row + dx, col + dy
                    if valid(next_row, next_col) and (next_row, next_col) not in visited:
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            stack.append((next_row, next_col))
                            visited.add((next_row, next_col))
            return False
        
        m = len(heights)
        n = len(heights[0])  # 1 <= rows, columns <= 100
        # determine domain space => min = 0, max = max(max(row) for row in heights)
        # the answer is guarenteed to exist (because we are asking for min in all possibilities)
        # therefore we use binary search find algo instead of insertion algo
        left = 0
        right = max(max(row) for row in heights)
        while left <= right:
            mid = (left + right) // 2
            if successful(mid):  # if successful go left to hopefully find a smaller value
                right = mid - 1
            else:
                left = mid + 1
        return left

        
