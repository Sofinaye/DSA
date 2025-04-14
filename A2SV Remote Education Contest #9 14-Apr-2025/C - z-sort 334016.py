# Problem: C - z-sort - https://codeforces.com/gym/603156/problem/C

n = int(input())
a = list(map(int, input().split(" ")))
a.sort()
result = [0] * n
left = 0
right = n - 1

for i in range(n):
    if i % 2 == 0:
        result[i] = a[left]
        left += 1
    else:
        result[i] = a[right]
        right -= 1

print(" ".join(map(str, result)))
