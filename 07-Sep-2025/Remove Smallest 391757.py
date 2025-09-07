# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()
    valid = True
    for i in range(1, n):
        if arr[i] - arr[i-1] > 1:
            valid = False
            break
    print("YES" if valid else "NO")