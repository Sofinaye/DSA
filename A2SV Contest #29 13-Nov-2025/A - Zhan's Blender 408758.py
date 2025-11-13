# Problem: A - Zhan's Blender - https://codeforces.com/gym/633600/problem/A

t = int(input().strip())
result = []
for _ in range(t):
    n = int(input().strip())
    x, y = map(int, input().split())
    if n == 0:
        result.append("0")
    else:
        if y >= x:
            seconds = (n + x - 1) // x
            result.append(str(seconds))
        else:
            seconds = (n + y - 1) // y
            result.append(str(seconds))

print("\n".join(result))
