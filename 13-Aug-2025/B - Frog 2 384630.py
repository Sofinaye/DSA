# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

n, k = map(int, input().split())
h = list(map(int, input().split()))
INF = float('inf')

dp = [INF] * n
dp[0] = 0

for i in range(1, n):
    start = max(0, i - k)
    min_cost = INF
    for j in range(start, i):
        current_cost = dp[j] + abs(h[i] - h[j])
        if current_cost < min_cost:
            min_cost = current_cost
    dp[i] = min_cost

print(dp[-1])