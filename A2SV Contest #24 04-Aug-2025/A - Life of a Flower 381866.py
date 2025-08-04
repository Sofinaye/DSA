# Problem: A - Life of a Flower - https://codeforces.com/gym/626626/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = [0 for i in range(n)]
    res[0] = 1

    height = 1
    dead = False
    for i in range(n):
        if i > 0 and a[i] == 0 and a[i-1] == 0:
            dead = True
            break
    if dead:
        print(-1)
    else:
        for i in range(n):
            if a[i] == 1:
                if i > 0 and a[i-1] == 1:
                    height += 5
                else:
                    height += 1
        print(height)
