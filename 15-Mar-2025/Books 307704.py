# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))
left = 0
books = 0
current_sum = 0

for right in range(n):
    current_sum += a[right]

    while current_sum > t:
        current_sum -= a[left]
        left += 1

    books = max(books, right - left + 1)

print(books)
