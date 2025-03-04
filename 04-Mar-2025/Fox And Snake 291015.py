# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n, m = list(map(int, input().split()))
is_last = True
for i in range(n):
    if i % 2 == 0:
        print("#"*m)
    else:
        if is_last:
            print("."*(m-1)+"#")
            is_last = False
        else:
            print("#"+"."*(m-1))
            is_last = True
