# Problem: A - Greed - https://codeforces.com/gym/649420/problem/A

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_cola = sum(a)

max1 = max2 = 0
for cap in b:
    if cap >= max1:
        max2 = max1
        max1 = cap
    elif cap > max2:
        max2 = cap

if max1 + max2 >= total_cola:
    print("YES")
else:
    print("NO")
