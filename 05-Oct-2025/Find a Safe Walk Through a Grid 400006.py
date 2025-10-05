# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        min_unsafe = [[float('inf')] * n for _ in range(m)]
        
        start_unsafe = 1 if grid[0][0] == 1 else 0
        if start_unsafe > health - 1:
            return False
        
        min_unsafe[0][0] = start_unsafe
        dq = deque()
        dq.append((0, 0, start_unsafe))
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while dq:
            r, c, unsafe = dq.popleft()
            if unsafe > min_unsafe[r][c]:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_unsafe = unsafe + (1 if grid[nr][nc] == 1 else 0)
                    if new_unsafe < min_unsafe[nr][nc] and new_unsafe <= health - 1:
                        min_unsafe[nr][nc] = new_unsafe
                        dq.append((nr, nc, new_unsafe))
        
        return min_unsafe[m-1][n-1] <= health - 1