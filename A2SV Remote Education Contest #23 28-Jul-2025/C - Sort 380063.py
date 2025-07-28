# Problem: C - Sort - https://codeforces.com/gym/625306/problem/C

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n, c = map(int, input().split())
        a = list(map(int, input().split()))

        teleporters = []
        for i in range(n):
            teleporters.append((i + 1 + a[i], i + 1, a[i]))

        teleporters.sort()

        total_cost = 0
        count = 0
        for cost, pos, a_cost in teleporters:
            if total_cost + cost <= c:
                total_cost += cost
                count += 1
            else:
                break
        results.append(count)

    print('\n'.join(map(str, results)))


solve()
