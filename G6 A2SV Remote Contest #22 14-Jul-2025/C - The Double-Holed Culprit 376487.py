# Problem: C - The Double-Holed Culprit - https://codeforces.com/gym/622136/problem/C

n = int(input())
p = list(map(int, input().split()))
result = []
for start in range(1, n + 1):
    visted = [False] * (n + 1)
    current = start
    while not visted[current]:
        visted[current] = True
        current = p[current - 1]

    result.append(current)
print(" ".join(map(str, result)))