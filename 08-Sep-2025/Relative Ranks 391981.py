# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rank_map = {}
        for idx, s in enumerate(sorted_scores):
            if idx == 0:
                rank_map[s] = "Gold Medal"
            elif idx == 1:
                rank_map[s] = "Silver Medal"
            elif idx == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(idx + 1)
        
        return [rank_map[s] for s in score]
