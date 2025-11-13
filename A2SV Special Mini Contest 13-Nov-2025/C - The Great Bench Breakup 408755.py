# Problem: C - The Great Bench Breakup - https://codeforces.com/gym/608569/problem/C

def is_valid(n, m, k, x):
    row_capacity = x * (m // (x + 1)) + (m % (x + 1))
    total_capacity = n * row_capacity
    return total_capacity >= k


def solve(n, m, k):
    low, high = 1, m
    answer = m

    while low <= high:
        mid = (low + high) // 2
        if is_valid(n, m, k, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    print(solve(n, m, k))
