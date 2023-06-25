from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Build rows hashmap (rows are the input), tuple as key
        # Example:
        # grid = [[3,2,1],[1,7,6],[2,7,7]]
        # row_map={
        #     (3,2,1): 0,
        #     (1,7,6): 1,
        #     (2,7,7): 2
        # }
        row_map = defaultdict(list)
        n = len(grid)
        for i in range(n):
            row_map[tuple(grid[i])].append(i)

        # Go through grid, look up hash map, construct result
        # result = []  # just need number of results
        num_result = 0
        for i in range(n):
            col = list()
            for j in range(n):
                col.append(grid[j][i])
            if tuple(col) in row_map:
                row_indices = row_map[tuple(col)]
                for row_index in row_indices:
                    # result.append([row_index, i])  # just need number of results
                    num_result += 1
        # return result  # just need number of results
        return num_result


