# Problem: C - Permutation Partitions - https://codeforces.com/gym/649420/problem/C

MOD = 998244353

n, k = map(int, input().split())
p = list(map(int, input().split()))

arr = [(val, idx) for idx, val in enumerate(p)]
arr.sort(reverse=True)

top_k_indices = [idx for val, idx in arr[:k]]
top_k_indices.sort()

max_value = sum(val for val, idx in arr[:k])

ways = 1
for i in range(1, k):
    ways = (ways * (top_k_indices[i] - top_k_indices[i-1])) % MOD

print(max_value, ways)
