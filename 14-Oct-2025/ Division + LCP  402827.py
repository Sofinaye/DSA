# Problem:  Division + LCP  - https://codeforces.com/contest/1968/problem/G1

nxt = [0] * 200010


def kmp(m):
    global nxt, s, n
    c = 0
    for i in range(1, m):
        v = s[i]
        while c and v != s[c]:
            c = nxt[c - 1]
        if v == s[c]:
            c += 1
        nxt[i] = c

    cnt = 0
    c = 0
    for i in range(n):
        v = s[i]
        while c and v != s[c]:
            c = nxt[c - 1]
        if v == s[c]:
            c += 1
        if c == m:
            cnt += 1
            c = 0
    return cnt


def solve():
    global s, n
    n, l, r = map(int, input().split())
    k = l
    s = input().strip()
    L, R = 1, n
    while L <= R:
        mid = (L + R) >> 1
        if kmp(mid) >= k:
            L = mid + 1
        else:
            R = mid - 1
    print(R)


t = int(input())
for test in range(1, t + 1):
    solve()
