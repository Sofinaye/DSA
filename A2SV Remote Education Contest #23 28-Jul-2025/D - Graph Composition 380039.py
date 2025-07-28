# Problem: D - Graph Composition - https://codeforces.com/gym/625306/problem/D

def solve():
    t = int(input())
    for _ in range(t):
        n, m1, m2 = map(int, input().split())
        fsl = [[] for _ in range(n)]
        gsl = [[] for _ in range(n)]
        for _ in range(m1):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            fsl[u].append(v)
            fsl[v].append(u)
        for _ in range(m2):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            gsl[u].append(v)
            gsl[v].append(u)

        gcol = [0]*n
        for i in range(n):
            if gcol[i] == 0:
                c = i+1
                stack = [i]
                gcol[i] = c
                while stack:
                    u = stack.pop()
                    for v in gsl[u]:
                        if gcol[v] == 0:
                            gcol[v] = c
                            stack.append(v)

        fcol = [0]*n
        ans = 0
        for i in range(n):
            if fcol[i] == 0:
                c = gcol[i]
                stack = [i]
                fcol[i] = c
                while stack:
                    u = stack.pop()
                    for v in fsl[u]:
                        if fcol[v] == 0:
                            if gcol[v] != c:
                                ans += 1
                            else:
                                fcol[v] = c
                                stack.append(v)
                if gcol[i] < i+1:
                    ans += 1

        print(ans)


solve()
