# Problem: A - Melody Perfection - https://codeforces.com/gym/628023/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    condition = True
    for i in range(1, n):
        diff = abs(a[i] - a[i - 1])
        if diff != 7 and diff != 5:
            condition = False
            break

    if condition:
        print("YES")
    else:
        print("NO")