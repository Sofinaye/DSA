# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
h = list(map(int, input().split()))

if n == 2:
    print(abs(h[0] - h[1]))
else:
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(h[0] - h[1])
    for i in range(2, n):
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))
    print(dp[n-1])