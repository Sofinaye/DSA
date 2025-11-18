# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

n, d = map(int, input().split())
friends = []
for _ in range(n):
    m, s = map(int, input().split())
    friends.append((m, s))
 
friends.sort()  # sort by money
 
left = 0
current_sum = 0
max_sum = 0
 
for right in range(n):
    current_sum += friends[right][1]
    while friends[right][0] - friends[left][0] >= d:
        current_sum -= friends[left][1]
        left += 1
    max_sum = max(max_sum, current_sum)
 
print(max_sum)