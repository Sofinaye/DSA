# Problem: D - Vasya’s Holiday Schedule - https://codeforces.com/gym/628023/problem/D

n = int(input())
a = list(map(int, input().split()))

dp = [[float('inf')] * 3 for _ in range(n)]

if a[0] == 0:
    dp[0][0] = 1
elif a[0] == 1:
    dp[0][0] = 1
    dp[0][1] = 0
elif a[0] == 2:
    dp[0][0] = 1
    dp[0][2] = 0
elif a[0] == 3:
    dp[0][0] = 1
    dp[0][1] = 0
    dp[0][2] = 0

for i in range(1, n):
    dp[i][0] = 1 + min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
    if a[i] in [1, 3]:
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])

    if a[i] in [2, 3]:
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])

result = min(dp[n - 1][0], dp[n-1][1], dp[n - 1][2])
print(result)
