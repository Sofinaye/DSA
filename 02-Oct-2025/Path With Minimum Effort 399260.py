# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        diff_mat = [[float('inf')] * col  for _ in range(row)]
        diff_mat[0][0] = 0
        vis = [[False] * col for _ in range(row)]
        q = [(0, 0, 0)]

        while q:
            diff, x, y = heapq.heappop(q)
            vis[x][y] = True

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                newX = x + dx
                newY = y + dy
                if 0 <= newX < row and 0 <= newY < col and not vis[newX][newY]:
                    curr_diff = abs(heights[newX][newY] - heights[x][y])
                    max_diff = max(curr_diff, diff_mat[x][y])
                    if diff_mat[newX][newY] > max_diff:
                        diff_mat[newX][newY] = max_diff
                        heapq.heappush(q, (max_diff, newX, newY))
        return diff_mat[row - 1][col - 1]

