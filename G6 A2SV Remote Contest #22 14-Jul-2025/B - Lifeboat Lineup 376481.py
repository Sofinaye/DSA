# Problem: B - Lifeboat Lineup - https://codeforces.com/gym/622136/problem/B

n = int(input())
crew = []
for i in range(n):
    name, status = input().split()
    crew.append((name, status, i))
priority_order = {'rat': 0, 'woman': 1, 'child': 1, 'man': 2, 'captain': 3}

crew_with_priority = []
for member in crew:
    name, status, original_index = member
    priority = priority_order[status]
    crew_with_priority.append((priority, original_index, name))

crew_sorted = sorted(crew_with_priority, key=lambda x: (x[0], x[1]))

for member in crew_sorted:
    print(member[2])
