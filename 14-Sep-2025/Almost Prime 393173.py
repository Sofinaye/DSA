# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def solve(n):
    count = 0
    for num in range(1, n+1):
        distinct_primes = set()
        temp = num
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                distinct_primes.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            distinct_primes.add(temp)
        if len(distinct_primes) == 2:
            count += 1
    return count


n = int(input().strip())
print(solve(n))