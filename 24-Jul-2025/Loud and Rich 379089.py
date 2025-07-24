# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        ind = [0] * n
        res = [i for i in range(n)]

        for rich, poor in richer:
            graph[rich].append(poor)
            ind[poor] += 1

        queue = deque()

        for i in range(n):
            if ind[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()

            for neigbhor in graph[curr]:
                curr_quiet = res[curr]
                nei_quiet = res[neigbhor]

                if quiet[curr_quiet] < quiet[nei_quiet]:
                    res[neigbhor] = curr_quiet

                ind[neigbhor] -= 1
                if ind[neigbhor] == 0:
                    queue.append(neigbhor)
        return res