class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # right, down, left, up
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isEdge(r, c):
            return r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0])

        # traverse to the right until edge or visited
        # traverse to the bottom until edge or visited
        # traverse to the left until edge or visited
        # traverse to the top until edge or visited
        direction = 0
        row, col = 0, 0
        res = []
        while not isEdge(row, col) and matrix[row][col] != -999:
            res.append(matrix[row][col])
            matrix[row][col] = -999

            (dr, dc) = step[direction % 4]

            if isEdge(row + dr, col + dc) or matrix[row + dr][col + dc] == -999:
                matrix[row][col] = -999
                direction += 1
                (dr, dc) = step[direction % 4]

            row += dr
            col += dc

        return res
