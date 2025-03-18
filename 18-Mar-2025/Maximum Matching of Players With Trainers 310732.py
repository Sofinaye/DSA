# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        trainers.sort()
        players.sort()
        player = trainer = count = 0
        n, m = len(players), len(trainers)

        while player < n and trainer < m:
            if players[player] <= trainers[trainer]:
                count += 1
                player += 1
                trainer += 1
            else:
                trainer += 1

        return count
        
        
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        