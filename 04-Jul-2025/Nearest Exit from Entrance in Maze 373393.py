# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0]) if rows > 0 else 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = '+'  
        
        while queue:
            x, y, steps = queue.popleft()
            
            if (x == 0 or x == rows - 1 or y == 0 or y == cols - 1) and [x, y] != entrance:
                return steps
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'  
                    queue.append((nx, ny, steps + 1))
        
        return -1
