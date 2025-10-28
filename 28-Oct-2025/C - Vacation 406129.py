# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

def main():
    N = int(input())
    a, b, c = [], [], []
    for _ in range(N):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    
    dp = [[0]*3 for _ in range(N)]
    dp[0][0] = a[0]
    dp[0][1] = b[0]
    dp[0][2] = c[0]
    
    for i in range(1, N):
        dp[i][0] = a[i] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = b[i] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = c[i] + max(dp[i-1][0], dp[i-1][1])
    
    print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

if __name__ == "__main__":
    main()