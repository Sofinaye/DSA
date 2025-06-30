# Problem: A - Coins - https://codeforces.com/gym/618729/problem/A

t = int(input())
res = []
for _ in range(t):
    n, k = map(int, input().split())

    y = n // k

    remaining = n - y * k

    if remaining % 2 == 0:
        res.append("YES")
    else:
        if y > 0 and (n - k * (y - 1)) % 2 == 0:
            res.append("YES")
        else:
            res.append("NO")

for result in res:
    print(result)