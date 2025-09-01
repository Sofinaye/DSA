# Problem: A - Loopix: Multiples Hunt - https://codeforces.com/gym/632067/problem/A

def solve():
    l, r, k = map(int, input().split())
    if k == 1:
        print(r - l + 1)
        return

    if l == r:
        if k == 1:
            print(1)
        else:
            print(0)

        return

    if l > (r // k):
        print(0)
    else:
        count = (r // k) - l + 1
        print(count)


t = int(input())
for _ in range(t):
    solve()
