class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def get_valid_neighbors(row, col, visited):
            valid_neighbors = []
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # left, right, up, down
            for row_diff, col_diff in directions:
                neighbor_row = row + row_diff
                neighbor_col = col + col_diff
                if 0 <= neighbor_row < m and 0 <= neighbor_col < n and (neighbor_row, neighbor_col) not in visited:  # do not go backwards
                    valid_neighbors.append((neighbor_row, neighbor_col))
            return valid_neighbors
        
        def backtrack(curr_str, row, col, word_index, visited):
            # print(f'==== backtrack curr_str={curr_str}, row={row}, col={col}, word_index={word_index}, visited={visited}')
            # Base condition - we found the word, or length exceeds word's length.
            # IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # WE HAVE TO USE nonlocal HERE OTHERWISE THE VALUE OF word_exist OUTSIDE OF
            # THIS FUNCITON WILL NEVER CHANGE!!!!
            # EVEN THOUGH PYTHON COMPLAINS ABOUT AN UNDEFINED VARIABLE FOR EXAMPLE
            # name 'x' is not defined
            # BUT WHEN IT IS IN THE INNER FUNCTION IT DOES NOT COMPLAIN!!!!!!!!!!!!!!!! 
            # THAT IS JUST WEIRD AND INCONSISTENT :-(
            nonlocal word_exist
            if curr_str == word:
                # print(f'FOUND!!!! curr_str={curr_str}, word={word}')
                word_exist = True
                return
            elif len(curr_str) > len(word):
                return  # DO NOT SET ANYTHING HERE! DEFAULT IS FALSE UNLESS THERE IS ANY TRUE!
            valid_neighbors = get_valid_neighbors(row, col, visited)
            # print(f'valid_neighbors={valid_neighbors}')
            for neighbor_row, neighbor_col in valid_neighbors:
                neighbor_char = board[neighbor_row][neighbor_col]
                # At this point, word_index is guarenteed to be < len(word) - 1
                if word_index + 1 < len(word) and neighbor_char != word[word_index + 1]:
                    continue
                curr_str += neighbor_char
                visited.append((neighbor_row, neighbor_col))
                backtrack(curr_str, neighbor_row, neighbor_col, word_index + 1, visited)
                curr_str = curr_str[:-1]
                visited.pop()

        m = len(board)  # rows
        n = len(board[0])  # cols # 1 <= m, n <= 6
        word_exist = False
        for row in range(0, m):
            for col in range(0, n):
                # MY SOLUTION EXCEDDED TIME LIMIT FOR TEST CASE:
                # board = [["A","A","A","A","A","A"],
                #          ["A","A","A","A","A","A"],
                #          ["A","A","A","A","A","A"],
                #          ["A","A","A","A","A","A"],
                #          ["A","A","A","A","A","A"],
                #          ["A","A","A","A","A","A"]]
                # word = "BAAAAAAAAAAAAAA"
                # IF THE FIRST CHAR DOES NOT MATCH, WE SHOULD IMMEDIATELY ABANDON THE PATH!
                # THIS IS ANOTHER IMPROVEMENT....
                if board[row][col] != word[0]:  # 1 <= word.length <= 15
                    continue
                # print(f'++++++++++++++++')
                # print(f'Exploring row={row}, col={col}, word_exist={word_exist}')
                if word_exist:  # IMPROVEMENT - IF WE HAVE FOUND THE WORD, NO NEED TO GO MORE!
                    break
                backtrack(board[row][col], row, col, 0, [(row, col)])
        return word_exist

# # Output example
# ++++++++++++++++
# Exploring row=0, col=0, word_exist=False
# ==== backtrack curr_str=A, row=0, col=0, word_index=0, visited=[(0, 0)]
# valid_neighbors=[(0, 1), (1, 0)]
# ==== backtrack curr_str=AB, row=0, col=1, word_index=1, visited=[(0, 0), (0, 1)]
# valid_neighbors=[(0, 2), (1, 1)]
# ==== backtrack curr_str=ABC, row=0, col=2, word_index=2, visited=[(0, 0), (0, 1), (0, 2)]
# valid_neighbors=[(0, 3), (1, 2)]
# ==== backtrack curr_str=ABCC, row=1, col=2, word_index=3, visited=[(0, 0), (0, 1), (0, 2), (1, 2)]
# valid_neighbors=[(1, 1), (1, 3), (2, 2)]
# ==== backtrack curr_str=ABCCE, row=2, col=2, word_index=4, visited=[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
# valid_neighbors=[(2, 1), (2, 3)]
# ==== backtrack curr_str=ABCCED, row=2, col=1, word_index=5, visited=[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1)]
# FOUND!!!! curr_str=ABCCED, word=ABCCED
# ++++++++++++++++
# Exploring row=0, col=1, word_exist=True
# ++++++++++++++++
# Exploring row=1, col=0, word_exist=True
# ++++++++++++++++
# Exploring row=2, col=0, word_exist=True

