# Problem: B - Counting Without Divisibility - https://codeforces.com/gym/608569/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = (k - 1) // (n - 1)
    pos = k - m * (n - 1)
    print(m * n + pos)