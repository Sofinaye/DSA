# Problem: C - Loopix: The Book Cycle - https://codeforces.com/gym/632067/problem/C

q = int(input())
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    p = [x-1 for x in p]
    visited = [False]*n
    result = [0]*n

    for i in range(n):
        if not visited[i]:
            cycle = []
            x = i
            while not visited[x]:
                cycle.append(x)
                visited[x] = True
                x = p[x]
            cycle_len = len(cycle)
            for node in cycle:
                result[node] = cycle_len

    print(*result)