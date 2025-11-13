# Problem: A - Stairway to Goodness - https://codeforces.com/gym/608569/problem/A

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    result = 0
    count = 1
    while l <= r:
        result += 1
        l += count
        count += 1
    print(result)