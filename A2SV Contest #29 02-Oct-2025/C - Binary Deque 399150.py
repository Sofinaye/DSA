# Problem: C - Binary Deque - https://codeforces.com/gym/633600/problem/C

t = int(input().strip())
results = []
for _ in range(t):
    data = input().split()
    n = int(data[0])
    s = int(data[1])
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    if total_sum < s:
        results.append("-1")
    elif total_sum == s:
        results.append("0")
    else:
        left = 0
        current_ones = 0
        max_len = 0
        for right in range(len(arr)):
            current_ones += arr[right]
            while current_ones > s:
                current_ones -= arr[left]
                left += 1
            if current_ones == s:
                window_len = right - left + 1
                if window_len > max_len:
                    max_len = window_len
        operations = len(arr) - max_len
        results.append(str(operations))

print("\n".join(results))
