# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

from collections import defaultdict
import math
 
def solve():
    x = int(input())
    ls = [input() for _ in range(x)]
    mp = defaultdict(int)
    for i in range(x-1,-1,-1):
        if mp[ls[i]]==0:
            print(ls[i])
        mp[ls[i]] = 1
    
 
solve()
