# Problem: A - Swap to Max - https://codeforces.com/gym/622136/problem/A

t = int(input())
for _ in range(t):
    l = int(input())
    A = float('-inf')
    B = float('-inf')
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(l):
        A = max(A, max(a[i], b[i]))
        B = max(B, min(a[i], b[i]))

    print(A * B)
