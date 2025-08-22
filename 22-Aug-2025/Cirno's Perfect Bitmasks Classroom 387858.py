# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

def is_power_of_two(n):
    return (n & (n - 1)) == 0


def main():
    t = int(input())
    index = 1
    results = []
    for _ in range(t):
        x = int(input())
        index += 1
        if not is_power_of_two(x):
            y = x & -x
            results.append(str(y))
        else:
            if x == 1:
                results.append("3")
            else:
                results.append(str(x | 1))
    print("\n".join(results))


main()
