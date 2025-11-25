# Problem: B - Two Arrays - https://codeforces.com/gym/649420/problem/B

t = int(input())
for _ in range(t):
    n, T = map(int, input().split())
    arr = list(map(int, input().split()))

    color = []
    flip = 0
    for x in arr:
        if 2 * x == T:
            color.append(flip)
            flip = 1 - flip
        elif 2 * x < T:
            color.append(0)
        else:
            color.append(1)

    print(' '.join(map(str, color)))