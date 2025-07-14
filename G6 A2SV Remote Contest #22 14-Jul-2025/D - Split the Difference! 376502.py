# Problem: D - Split the Difference! - https://codeforces.com/gym/622136/problem/D

n, k = map(int, input().split())
a = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    differences = []
    for i in range(1, n):
        differences.append(a[i] - a[i-1])

    differences.sort(reverse=True)
    total = a[-1] - a[0]
    if k > 1:
        total -= sum(differences[:k-1])
    print(total)
