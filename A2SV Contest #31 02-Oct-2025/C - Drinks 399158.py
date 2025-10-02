# Problem: C - Drinks - https://codeforces.com/gym/637748/problem/C

n = int(input())
p = list(map(int, input().split()))

average = sum(p) / n
print(f"{average:.12f}")