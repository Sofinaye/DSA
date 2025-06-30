# Problem: D - Serial Time! - https://codeforces.com/gym/618729/problem/D

from collections import deque


def solve():
    import sys
    input = sys.stdin.read().split('\n')
    ptr = 0
    k, n, m = map(int, input[ptr].split())
    ptr += 1

    grid = []
    for _ in range(k):
        layer = []
        while ptr < len(input) and input[ptr].strip() == '':
            ptr += 1
        for _ in range(n):
            if ptr >= len(input):
                row = ''
            else:
                row = input[ptr].strip()
            ptr += 1
            layer.append(list(row))
        grid.append(layer)

    while ptr < len(input) and input[ptr].strip() == '':
        ptr += 1
    if ptr < len(input):
        x, y = map(int, input[ptr].split())
    else:
        x, y = 1, 1
    x -= 1
    y -= 1

    if grid[0][x][y] == '#':
        print(0)
        return

    directions = [
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1)
    ]

    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(k)]
    queue = deque()
    queue.append((0, x, y))
    visited[0][x][y] = True
    count = 1

    while queue:
        l, i, j = queue.popleft()
        for dl, di, dj in directions:
            nl, ni, nj = l + dl, i + di, j + dj
            if 0 <= nl < k and 0 <= ni < n and 0 <= nj < m:
                if not visited[nl][ni][nj] and grid[nl][ni][nj] == '.':
                    visited[nl][ni][nj] = True
                    count += 1
                    queue.append((nl, ni, nj))

    print(count)


solve()
