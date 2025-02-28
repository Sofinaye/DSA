# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict


def count_valid_pairs(n, nums):
    b = [nums[i] - (i + 1) for i in range(n)]

    freq = defaultdict(int)
    for num in b:
        freq[num] += 1

    count = 0
    for key in freq:
        k = freq[key]
        if k >= 2:
            count += k * (k - 1) // 2

    return count


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(count_valid_pairs(n, nums))
