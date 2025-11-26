# Problem: A - Xorion and the Peaks - https://codeforces.com/gym/630556/problem/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k > (n - 1) // 2:
        print(-1)
        continue
    
    res = [0] * n
    large = n
    for i in range(k):
        res[2 * i + 1] = large
        large -= 1
    small = 1
    for i in range(n):
        if res[i] == 0:
            res[i] = small
            small += 1
    print(' '.join(map(str, res)))