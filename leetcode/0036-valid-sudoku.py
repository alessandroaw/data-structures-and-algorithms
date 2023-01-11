# array and hashing
# TC: O(rc)
# SC: O(rc)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # store coordinate of each value in the board
        # based on each value stored, check if there are any invalid value

        d = dict()

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if val != ".":
                    d[val] = d.get(val, []) + [(row, col)]

        for val, points in d.items():
            if len(points) == 1:
                continue

            col_d = dict()
            row_d = dict()
            seg_d = dict()

            for (row, col) in points:
                seg = f'{row // 3}{col // 3}'
                if row in row_d or col in col_d or seg in seg_d:
                    return False

                col_d[col] = True
                row_d[row] = True
                seg_d[seg] = True

        return True
