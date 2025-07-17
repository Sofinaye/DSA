# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0

        while target > 1 and maxDoubles:
            if target % 2:
                target -= 1
                moves += 1
            else:
                target //= 2
                moves += 1
                maxDoubles -= 1

        moves += target - 1

        return moves