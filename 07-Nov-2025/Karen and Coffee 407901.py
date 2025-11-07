# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import Counter
import sys 
input = sys.stdin.readline
l,r,w=map(int, input().split())
q=[0]*200002
for _ in range(l):
    a,b=map(int, input().split())
    q[a]+=1
    if b+1 <=200000:
        q[b+1]-=1

s=[]
p=0
for i in q:
    s.append(i+p)
    p+=i

admissible = [0] * (200000 +1)
prefix = [0] * (200000 +1)
for t in range(1, 200000 +1):
    admissible[t] = 1 if s[t] >= r else 0
    prefix[t] = prefix[t-1] + admissible[t]
output = []
for _ in range(w):
    a, b = map(int,  input().split())
    # ptr +=2
    res = prefix[b] - prefix[a-1]
    output.append(str(res))
print('\n'.join(output))