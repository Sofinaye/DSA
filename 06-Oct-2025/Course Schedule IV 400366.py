# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        for course in range(numCourses):
            queue = deque([course])
            visited = set([course])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        reachable[course][neighbor] = True
                        queue.append(neighbor)
        
        return [reachable[u][v] for u, v in queries]