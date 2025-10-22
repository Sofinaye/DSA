# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
        dp_prev = [[0] * n for _ in range(n)]
        dp_prev[row][column] = 1
        
        for step in range(1, k + 1):
            dp_curr = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        pr, pc = r - dr, c - dc
                        if 0 <= pr < n and 0 <= pc < n:
                            dp_curr[r][c] += dp_prev[pr][pc]
            dp_prev = dp_curr
        
        total = sum(sum(row) for row in dp_prev)
        return total / (8 ** k)