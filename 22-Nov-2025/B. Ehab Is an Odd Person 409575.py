# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = list(map(int, input().split()))

even = any(x % 2 == 0 for x in a)
odd = any(x % 2 == 1 for x in a)

if even and odd:
    a.sort()

print(*a)
