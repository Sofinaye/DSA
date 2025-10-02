# Problem: A - In Search of an Easy Problem - https://codeforces.com/gym/637748/problem/A

n = int(input())
res = list(map(int, input().split()))

if 1 in res:
    print("HARD")
else:
    print("EASY")
