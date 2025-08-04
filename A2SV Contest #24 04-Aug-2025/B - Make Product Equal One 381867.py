# Problem: B - Make Product Equal One - https://codeforces.com/gym/626626/problem/B

n = int(input())
a = list(map(int, input().split()))
total = 0
negatives = 0
zeros = 0

for num in a:
    if num < 0:
        total += -1 - num
        negatives += 1
    elif num > 0:
        total += num - 1
    else:
        total += 1
        zeros += 1

if negatives % 2:
    if zeros > 0:
        pass
    else:
        total += 2

print(total)
