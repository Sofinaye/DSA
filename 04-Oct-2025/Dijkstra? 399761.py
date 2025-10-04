# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

import heapq

INF = 10**15


def solve():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        a, b, w = map(int, input().split())
        idx += 3
        graph[a].append((b, w))
        graph[b].append((a, w))

    dist = [INF] * (n + 1)
    prev = [-1] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    if dist[n] == INF:
        print(-1)
        return

    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    print(' '.join(map(str, path)))


solve()
