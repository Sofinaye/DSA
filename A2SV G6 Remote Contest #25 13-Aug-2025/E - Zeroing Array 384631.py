# Problem: E - Zeroing Array - https://codeforces.com/gym/628023/problem/E

n = int(input())
a = list(map(int, input().split()))
total_sum = sum(a)
max_a = max(a)

if total_sum % 2 != 0:
    print("NO")
else:
    if max_a > total_sum - max_a:
        print("NO")
    else:
        print("YES")
