# Problem: B - Game of Mathletes - https://codeforces.com/gym/633600/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    A, B = 0, n-1
    count = 0
    while A < B:
        s = arr[A] + arr[B]
        if s == k:
            count += 1
            A += 1
            B -= 1
        elif s > k:
            B -= 1
        elif s < k:
            A += 1
    print(count)