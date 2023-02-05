class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isOverEdge(r, c):
            return r < 0 or r >= n or c < 0 or c >= n

        row, col = 0, 0
        count = 1
        step = 0
        res = [[0] * n for _ in range(n)]

        dr, dc = steps[step % 4]
        while not isOverEdge(row, col) and res[row][col] == 0:
            res[row][col] = count

            if isOverEdge(row + dr, col + dc) or res[row + dr][col + dc] != 0:
                step += 1
                dr, dc = steps[step % 4]

            row += dr
            col += dc

            count += 1

        return res
