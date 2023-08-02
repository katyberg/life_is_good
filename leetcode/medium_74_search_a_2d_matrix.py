class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Intuition:
        # Treat the 2d matrix as a single array, just need a function to convert index
        # to 2D format so that we can get the value
        # 1 <= m, n <= 100
        rows = len(matrix)  # m
        cols = len(matrix[0])  # n
        def get_num_at_index(index: int):
            row = index // cols
            col = index % cols
            return matrix[row][col]
        # from now on we can imagine it's a single big array of m * n length
        left = 0
        right = rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            if get_num_at_index(mid) == target:
                return True
            elif get_num_at_index(mid) > target:  # go left
                right = mid - 1
            else:  # < target  # go right
                left = mid + 1
        return False

        # print(f'rows={rows}')
        # print(f'cols={cols}')
        # for i in range(rows * cols):
        #     get_num_at_index(i)
        # # Output:
        # # rows=3
        # # cols=4
        # # index=0, row=0, col=0
        # # index=1, row=0, col=1
        # # index=2, row=0, col=2
        # # index=3, row=0, col=3
        # # index=4, row=1, col=0
        # # index=5, row=1, col=1
        # # index=6, row=1, col=2
        # # index=7, row=1, col=3
        # # index=8, row=2, col=0
        # # index=9, row=2, col=1
        # # index=10, row=2, col=2
        # # index=11, row=2, col=3

