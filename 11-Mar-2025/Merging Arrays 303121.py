# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []

pointer1 = 0
pointer2 = 0

for i in range(m + n):
    if pointer1 == n:
        result.extend(arr2[pointer2:])
        break
    elif pointer2 == m:
        result.extend(arr1[pointer1:])
        break

    if arr1[pointer1] < arr2[pointer2]:
        result.append(arr1[pointer1])
        pointer1 += 1
    elif arr1[pointer1] > arr2[pointer2]:
        result.append(arr2[pointer2])
        pointer2 += 1
    else:
        result.append(arr1[pointer1])
        result.append(arr2[pointer2])
        pointer2 += 1
        pointer1 += 1


print(*result)