# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input().strip())
nums = list(map(int, input().split()))

serja = left = dima = turn = 0
right = n - 1
while left <= right:
    if nums[left] >= nums[right]:
        chosen = nums[left]
        left += 1
    else:
        chosen = nums[right]
        right -= 1
    if turn == 0:
        serja += chosen
        turn = 1
    else:
        dima += chosen
        turn = 0


print(serja, dima)
