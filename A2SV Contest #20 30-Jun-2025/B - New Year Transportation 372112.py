# Problem: B - New Year Transportation - https://codeforces.com/gym/618729/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))
current = 1
reached = False
while current < n:
    next_cell = current + a[current - 1]
    if next_cell == t:
        reached = True
        break
    current = next_cell
print("YES" if reached else "NO")
