# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

def solve():
    n,m = map(int,input().split())
    arr =[[0] * n for i in range(n)]
    arr2 = [-1] * n
    arr2[0] = 0 
    arr3 = []
     
    for i in range(m):
        a, b = map(int,input().split())
        arr[b-1][a-1] = 1
        arr[a-1][b-1] = 1
     
    arr3.append(0)
    while(arr3):
        i = arr3.pop(0)  
        for j in range(n):
            if (arr[i][j] != arr[0][n-1]) and (arr2[j] == -1):
                arr2[j] = arr2[i]+1
                arr3.append(j)
     
    print(arr2[n-1])
        
        
solve()
    
    
    

    