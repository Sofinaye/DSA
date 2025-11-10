# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        streets = {
        1: [0, 1],
        2: [2, 3],
        3: [0, 3],
        4: [1, 3],
        5: [0, 2],
        6: [1, 2]
    }
        
        opposite = [1, 0, 3, 2]
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append((0, 0))
        visited[0][0] = True
        
        move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return True
            
            for d in streets[grid[r][c]]:
                nr, nc = r + move[d][0], c + move[d][1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                    continue
                # Check if neighbor can connect back to us
                incoming_dir = opposite[d]
                if incoming_dir in streets[grid[nr][nc]]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
        
        return False
