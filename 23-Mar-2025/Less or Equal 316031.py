# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

def solution(n, k, a):
    a.sort()

    if k == 0:
        return a[0] - 1 if a[0] > 1 else -1

    index = a[k-1]

    if k < n and a[k] == index:
        return -1

    if k < n and index + 1 < a[k]:
        return index + 1
    else:
        return index


n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solution(n, k, a))
